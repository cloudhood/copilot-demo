# Fuzzy match a name using Levenshtein distance and metaphone and return the best match.
def fuzzyMatch(name, names):
    """
    Fuzzy match a name using Levenshtein distance and metaphone and return the best match.
    :param name: string
    :param names: list of strings
    :return: string
    """
    import metaphone
    name = metaphone.metaphone(name)
    best_match = None
    best_distance = float('inf')
    for n in names:
        n = metaphone.metaphone(n)
        distance = Levenshtein.distance(name, n)
        if distance < best_distance:
            best_match = n
            best_distance = distance
    return best_match

# Implement k-means clustering from scratch.
def kMeansFromScratch(points, k, max_iterations):
    """
    Implement k-means clustering from scratch.
    :param points: list of tuples
    :param k: int
    :param max_iterations: int
    :return: list of tuples
    """
    from random import randint
    clusters = []
    for i in range(k):
        clusters.append([points[randint(0, len(points) - 1)]])
    for i in range(max_iterations):
        for cluster in clusters:
            cluster.clear()
        for point in points:
            min_distance = float('inf')
            min_cluster = None
            for cluster in clusters:
                distance = sum([(p[0] - point[0]) ** 2 + (p[1] - point[1]) ** 2 for p in cluster])
                if distance < min_distance:
                    min_distance = distance
                    min_cluster = cluster
            min_cluster.append(point)
        for cluster in clusters:
            x_sum = sum([p[0] for p in cluster])
            y_sum = sum([p[1] for p in cluster])
            cluster[0] = (x_sum / len(cluster), y_sum / len(cluster))
    return clusters


# Median of two sorted lists.
def median(lst):
    """
    Median of two sorted lists.
    :param lst: list
    :return: float
    """
    lst = sorted(lst)
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
    else:
        return lst[len(lst) // 2]

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. 
# The overall run time complexity should be O(log (m+n)).
def findMedianSortedArrays(nums1, nums2):
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. 
    The overall run time complexity should be O(log (m+n)).
    :param nums1: list
    :param nums2: list
    :return: float
    """
    nums1.extend(nums2)
    nums1.sort()
    return median(nums1)

# Given a string, find the length of the longest substring without repeating characters.
def lengthOfLongestSubstring(s):
    """
    Given a string, find the length of the longest substring without repeating characters.
    :param s: string
    :return: int
    """
    from collections import Counter
    c = Counter(s)
    max_len = 0
    start = 0
    for i, c in enumerate(s):
        if c in s[start:i]:
            max_len = max(max_len, i - start)
            start = s.index(c, start) + 1
    return max(max_len, len(s) - start)

# Predict whether the given number is a prime.
def isPrime(n):
    """
    Predict whether the given number is a prime.
    :param n: int
    :return: bool
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Fit a line to the given data points using least squares.
def fitLine(points):
    """
    Fit a line to the given data points using least squares.
    :param points: list of tuples
    :return: tuple
    """
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    x_diff = [p[0] - x_mean for p in points]
    y_diff = [p[1] - y_mean for p in points]
    x_diff_sq = [p[0] ** 2 for p in points]
    y_diff_sq = [p[1] ** 2 for p in points]
    x_diff_y_diff = [p[0] * p[1] for p in points]
    x_diff_sq_mean = sum(x_diff_sq) / len(x_diff_sq)
    y_diff_sq_mean = sum(y_diff_sq) / len(y_diff_sq)
    x_diff_y_diff_mean = sum(x_diff_y_diff) / len(x_diff_y_diff)
    m = (x_diff_y_diff_mean - x_diff_sq_mean * y_diff_sq_mean) / (x_diff_sq_mean - len(x_diff) * x_mean ** 2)
    b = y_diff_sq_mean - m * x_diff_sq_mean
    return m, b

# Implement k-means clustering.
def kMeans(points, k, max_iterations):
    """
    Implement k-means clustering.
    :param points: list of tuples
    :param k: int
    :param max_iterations: int
    :return: list of tuples
    """
    from random import randint
    clusters = []
    for i in range(k):
        clusters.append([points[randint(0, len(points) - 1)]])
    for i in range(max_iterations):
        for cluster in clusters:
            cluster.clear()
        for point in points:
            min_distance = float('inf')
            min_cluster = None
            for cluster in clusters:
                distance = sum([(p[0] - point[0]) ** 2 + (p[1] - point[1]) ** 2 for p in cluster])
                if distance < min_distance:
                    min_distance = distance
                    min_cluster = cluster
            min_cluster.append(point)
        for cluster in clusters:
            x_sum = sum([p[0] for p in cluster])
            y_sum = sum([p[1] for p in cluster])
            cluster[0] = (x_sum / len(cluster), y_sum / len(cluster))
    return clusters

# Implement k-nearest neighbors.
def kNearestNeighbors(points, k):
    """
    Implement k-nearest neighbors.
    :param points: list of tuples
    :param k: int
    :return: list of tuples
    """
    from heapq import nsmallest
    from math import sqrt
    neighbors = []
    for point in points:
        neighbors.append([])
        for point2 in points:
            neighbors[-1].append((sqrt((point[0] - point2[0]) ** 2 + (point[1] - point2[1]) ** 2), point2))
        neighbors[-1] = nsmallest(k, neighbors[-1])
    return neighbors

# Download a file from a URL.
def downloadFile(url):
    """
    Download a file from a URL.
    :param url: string
    :return: string
    """
    import urllib.request
    return urllib.request.urlopen(url).read()

# Youtube video downloader.
def downloadYoutubeVideo(url, filename):
    """
    Download a youtube video.
    :param url: string
    :param filename: string
    :return: string
    """
    import urllib.request
    import urllib.parse
    import urllib.error
    import re
    video_id = re.search(r'v=(\w+)', url).group(1)
    url = 'http://www.youtube.com/get_video?video_id=' + video_id
    urllib.request.urlretrieve(url, filename)

