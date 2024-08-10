def jaccard_similarity(query, name):
    # Convert both strings to lowercase and split them into words
    query_set = set(query.lower().split())
    name_set = set(name.lower().split())
    
    # Calculate the intersection and union of the two sets
    intersection = query_set.intersection(name_set)
    union = query_set.union(name_set)
    
    # Return the Jaccard similarity (intersection size divided by union size)
    if union:
        return len(intersection) / len(union)
    return 0

def search_names_with_jaccard(query, names):
    # Calculate Jaccard similarity for each name
    similarities = [(name, jaccard_similarity(query, name)) for name in names]
    # Sort names by similarity score (highest first)
    sorted_names = sorted(similarities, key=lambda x: x[1], reverse=True)
    # Filter results with a non-zero similarity score
    top_results = [name for name, score in sorted_names if score > 0]
    print(top_results)
    return top_results
