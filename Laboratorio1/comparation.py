import matplotlib.pyplot as plt

def parse_cachegrind(file_path):
    """Parse a cachegrind file and return a dictionary of function names and their cache misses."""
    cache_data = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            if line.startswith('fl='):
                continue
            if line.startswith('fn='):
                parts = line.strip().split(' ')
                func_id = parts[0].split('=')[1]
                func_name = ' '.join(parts[1:])
                cache_data[func_name] = 0
            elif line.startswith('calls='):
                continue
            elif line.startswith('caches='):
                parts = line.strip().split(' ')
                func_id = parts[0].split('=')[1]
                cache_misses = int(parts[1])
                func_name = next(name for name in cache_data.keys() if name.startswith(func_id))
                cache_data[func_name] = cache_misses
    return cache_data

def compare_cachegrind(file1, file2):
    """Compare cachegrind data from two files and return a dictionary of differences."""
    data1 = parse_cachegrind(file1)
    data2 = parse_cachegrind(file2)
    
    all_functions = set(data1.keys()).union(set(data2.keys()))
    differences = {}
    
    for func in all_functions:
        misses1 = data1.get(func, 0)
        misses2 = data2.get(func, 0)
        differences[func] = misses2 - misses1
    
    return differences

def plot_differences(differences):
    """Plot the differences between cachegrind files."""
    functions = list(differences.keys())
    diff_values = list(differences.values())
    
    plt.figure(figsize=(12, 8))
    plt.barh(functions, diff_values, color='skyblue')
    plt.xlabel('Difference in Cache Misses')
    plt.title('Differences in Cache Misses Between Two Cachegrind Files')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    file1 = r'C:\UCSP\Paralela\bloques.cachegrind'
    file2 = r'C:\UCSP\Paralela\clasica.cachegrind'
    
    differences = compare_cachegrind(file1, file2)
    plot_differences(differences)
