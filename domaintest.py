import requests

INPUT_FILE = 'url.txt'
OUTPUT_FILE = 'http_responses.txt'

def read_domains_from_file(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def check_http_responses(domains):
    results = []
    for domain in domains:
        try:
            response = requests.get(domain, timeout=5)
            results.append(f"[{response.status_code}] {domain} - OK")
        except requests.exceptions.RequestException as e:
            results.append(f"[ERROR] {domain} - {str(e)}")
    return results

def write_results_to_file(results, file_path):
    with open(file_path, 'w') as f:
        for line in results:
            f.write(line + '\n')
    print(f"\nResults saved to '{file_path}'")

def main():
    domains = read_domains_from_file(INPUT_FILE)
    print(f"Checking {len(domains)} domains...\n")
    results = check_http_responses(domains)
    for line in results:
        print(line)
    write_results_to_file(results, OUTPUT_FILE)

if __name__ == "__main__":
    main()

