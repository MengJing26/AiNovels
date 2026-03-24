#!/usr/bin/env python3
"""
Unification Score Calculator
计算系统统一度 U = |V_intersect| / |⋃ Vᵢ|
"""

import json
import sys
from pathlib import Path

def load_yaml_variables(filepath):
    """Load variable sets from YAML description of services/systems"""
    import yaml
    with open(filepath, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    variable_sets = []
    for service_name, vars_list in data.get('services', {}).items():
        variable_sets.append(set(vars_list))

    return variable_sets

def calculate_unification_score(variable_sets):
    """Calculate unification score U"""
    if not variable_sets:
        return 0.0

    union = set()
    intersection = variable_sets[0].copy()

    for vs in variable_sets:
        union |= vs
        intersection &= vs

    u = len(intersection) / len(union) if union else 0
    return round(u, 4)

def analyze_fragmentation(variable_sets):
    """Generate fragmentation analysis report"""
    u = calculate_unification_score(variable_sets)

    print(f"🔍 Unification Analysis")
    print(f"{'='*40}")
    print(f"Services/Systems: {len(variable_sets)}")
    print(f"Union (total variables): {len(set().union(*variable_sets))}")
    print(f"Intersection (shared): {len(set.intersection(*variable_sets))}")
    print(f"Unification Score U: {u:.2%}")
    print()

    if u >= 0.7:
        status = "✅ HIGHLY UNIFIED"
    elif u >= 0.4:
        status = "⚠️  PARTIALLY UNIFIED"
    else:
        status = "❌ HIGHLY FRAGMENTED"
    print(f"Status: {status}")

    return u

def example_ecommerce():
    """Example: calculate unification score for e-commerce"""
    services = {
        "Orders": {"user_id", "order_id", "amount", "status", "items"},
        "Payments": {"user_id", "txn_id", "amount", "status", "method"},
        "Customer": {"user_id", "name", "email", "phone", "tier"},
        "Inventory": {"sku", "warehouse_id", "quantity", "location"},
        "Shipping": {"order_id", "tracking_no", "carrier", "address"}
    }

    variable_sets = [set(vars) for vars in services.values()]

    print("📦 E-commerce Services Analysis")
    for name, vars in services.items():
        print(f"  {name}: {len(vars)} variables")

    u = analyze_fragmentation(variable_sets)

    # Suggest core variables
    all_vars = set().union(*variable_sets)
    freq = {}
    for var in all_vars:
        count = sum(1 for vs in variable_sets if var in vs)
        freq[var] = count

    print("\n📊 Variable Frequency (appears in N services):")
    for var, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"  {var}: {count}/{len(variable_sets)}")

    return u

if __name__ == "__main__":
    # Run example
    example_ecommerce()

    # CLI usage: python unification_score.py services.yaml
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        vs = load_yaml_variables(filepath)
        u = analyze_fragmentation(vs)
        sys.exit(0 if u >= 0.7 else 1)
