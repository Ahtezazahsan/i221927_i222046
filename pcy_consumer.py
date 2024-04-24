from kafka import KafkaConsumer
from collections import defaultdict
from itertools import combinations

def generate_candidates(itemset, k):
    return set([i.union(j) for i in itemset for j in itemset if len(i.union(j)) == k])

def hashing_buckets(count_of_bucket, baskets, threshold):
    buckets = [0] * count_of_bucket
    for basket in baskets:
        for i, j in combinations(basket, 2):
            index = (i + j) % count_of_bucket
            buckets[index] += 1
    frequent_buckets = set([i for i, v in enumerate(buckets) if v >= threshold])
    return frequent_buckets

def prune_itemset(itemset, transactions, min_support, freq_items, bucket_count, threshold, frequent_buckets):
    candidate_counts = defaultdict(int)
    for item in itemset:
        for transaction in transactions:
            if item.issubset(transaction):
                candidate_counts[item] += 1

    pruned_itemset = set()
    local_freq_items = set()
    total_transactions = len(transactions)
    for item, count in candidate_counts.items():
        support = count / total_transactions
        if support >= min_support:
            pruned_itemset.add(item)
            local_freq_items.add(item)
            freq_items[item] = support

    pair_counts = defaultdict(int)
    for basket in transactions:
        frequent_items = [item for item in basket if item in frequent_buckets]
        for i, j in combinations(frequent_items, 2):
            if (i, j) in itemset or (j, i) in itemset:
                pair_counts[frozenset([i, j])] += 1
    for pair, count in pair_counts.items():
        support = count / total_transactions
        if support >= min_support:
            pruned_itemset.add(pair)
            local_freq_items.add(pair)
            freq_items[pair] = support
    return pruned_itemset, local_freq_items

def pcy(transactions, min_support):
    freq_items = {}
    candidate_itemset = set()
    for transaction in transactions:
        for item in transaction:
            candidate_itemset.add(frozenset([item]))

    count_of_bucket = 100
    threshold = min_support * len(transactions)
    frequent_buckets = hash_buckets(count_of_bucket, transactions, threshold)
    k = 2
    current_freq_items = set()
    while True:
        current_freq_items, local_freq_items = prune_itemset(candidate_itemset, transactions, min_support, freq_items, count_of_bucket, threshold, frequent_buckets)
        if len(current_freq_items) == 0:
            break
        freq_items.update(local_freq_items)
        candidate_itemset = generate_candidates(current_freq_items, k)
        k += 1
    return freq_items

def consume_data():
    consumer = KafkaConsumer('preprocessed_data', bootstrap_servers=['localhost:9092'],
                             auto_offset_reset='earliest', group_id=None)

    transactions = []
    for message in consumer:
        data = json.loads(message.value.decode('utf-8'))
        transactions.append(data['categories'])

        frequent_items = pcy(transactions, 0.1)
        print("\nFrequent Itemsets (PCY Algorithm):")
        for itemset, support in frequent_items.items():
            print(f"{itemset}: {support}")

if _name_ == "_main_":
    consume_data()
