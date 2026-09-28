from client import AgentContextDynamicCompressor
import json

def test():
    c = AgentContextDynamicCompressor()
    print("=== Testing Agent Context Dynamic Compressor ===")
    res = c.run_benchmark_compression()
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    test()
