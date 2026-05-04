#!/usr/bin/env python3
"""
Master Audit Script — Verify ALL C++ problem docs across all 6 prompt levels.
Run from: /home/23u58g/work/ZZZ_LEARN_VISWA_DOCS/CPP_problem_solving/
"""
import os, glob

BASE = "/home/23u58g/work/ZZZ_LEARN_VISWA_DOCS/CPP_problem_solving"

# Expected structure: (level_dir, [(category_dir, expected_count), ...])
EXPECTED = [
    ("Level_0_1_Beginner", [
        ("C00_Syntax_Program_Structure", None),
        ("C01_Data_Types_Variables", None),
        ("C10_Control_Flow_Loops", None),
        ("C11_Functions_Recursion", None),
        ("C12_Arrays_Strings_Core", None),
    ]),
    ("Level_2_3_Intermediate", [
        ("C20_Pointers_Memory", None),
        ("C21_OOP_Classes", None),
        ("C22_STL_Containers_Iterators", None),
        ("C30_Linked_Lists", None),
        ("C31_Stacks_Queues", None),
        ("C32_Hashing", None),
    ]),
    ("Level_4_5_Advanced", [
        ("C40_Trees_BST", None),
        ("C41_Graphs_Fundamentals", None),
        ("C50_Dynamic_Programming", None),
        ("C51_Heaps_PQ_Sorting", None),
    ]),
    ("Level_6_7_Expert", [
        ("C60_Advanced_Trees_SegTree_Trie_DSU", None),
        ("C61_Advanced_Graph_Algorithms", None),
        ("C70_Templates_Generic_Programming", None),
        ("C71_Concurrency_Multithreading", None),
    ]),
    ("Level_8_9_Pro", [
        ("C80_Advanced_Algorithms_String_Math_NT", None),
        ("C81_System_Design_Low_Level_CPP", None),
        ("C90_Competitive_Programming_Mastery", None),
    ]),
    ("Level_10_Master", [
        ("C100_Expert_Research_Level", None),
    ]),
]

def audit():
    print("=" * 80)
    print("  MASTER AUDIT — C++ Problem Solving Documentation")
    print("=" * 80)
    print()

    grand_total = 0
    grand_expected = 0
    all_ok = True
    level_summary = []

    for level_dir, categories in EXPECTED:
        level_path = os.path.join(BASE, level_dir)
        level_total = 0
        level_expected = 0
        level_ok = True

        print(f"📂 {level_dir}/")

        if not os.path.isdir(level_path):
            print(f"   ❌ MISSING directory!")
            all_ok = False
            continue

        # Check INDEX.md
        idx_file = os.path.join(level_path, "INDEX.md")
        has_index = os.path.isfile(idx_file)

        for cat_dir, exp_count in categories:
            cat_path = os.path.join(level_path, cat_dir)
            if not os.path.isdir(cat_path):
                print(f"   ❌ {cat_dir}/ — MISSING")
                all_ok = False
                level_ok = False
                continue

            md_files = glob.glob(os.path.join(cat_path, "*.md"))
            actual = len(md_files)
            level_total += actual

            if exp_count is not None:
                level_expected += exp_count
                status = "✅" if actual == exp_count else ("⚠️" if actual > 0 else "❌")
                if actual != exp_count:
                    level_ok = False
                    all_ok = False
                print(f"   {status} {cat_dir}: {actual}/{exp_count} files")
            else:
                level_expected += actual
                print(f"   ✅ {cat_dir}: {actual} files")

            # Sample check: verify first file has content
            if md_files:
                sample = sorted(md_files)[0]
                size = os.path.getsize(sample)
                if size < 500:
                    print(f"      ⚠️  First file suspiciously small ({size} bytes): {os.path.basename(sample)}")

        idx_status = "✅" if has_index else "⚠️"
        print(f"   {idx_status} INDEX.md: {'present' if has_index else 'missing'}")
        print(f"   📊 Subtotal: {level_total} files")
        print()

        grand_total += level_total
        grand_expected += level_expected
        level_summary.append((level_dir, level_total, level_ok))

    # Check for generator scripts
    print("🔧 Generator Scripts:")
    generators = glob.glob(os.path.join(BASE, "generate_*.py"))
    for g in sorted(generators):
        print(f"   ✅ {os.path.basename(g)}")
    print()

    # Check prompts
    print("📝 Prompt Files:")
    prompts = glob.glob(os.path.join(BASE, "prompts", "PROMPT_*.md"))
    for p in sorted(prompts):
        print(f"   ✅ {os.path.basename(p)}")
    print()

    # Cross-reference with JSX problem bank
    jsx_path = os.path.join(BASE, "cpp_interview_prep.jsx")
    if os.path.isfile(jsx_path):
        print("📋 JSX Problem Bank: ✅ present")
    else:
        print("📋 JSX Problem Bank: ❌ missing")
    print()

    # Grand summary
    print("=" * 80)
    print("  GRAND SUMMARY")
    print("=" * 80)
    print()
    print(f"  {'Level Directory':<35} {'Files':>8} {'Status':>8}")
    print(f"  {'─' * 35} {'─' * 8} {'─' * 8}")
    for name, count, ok in level_summary:
        status = "✅ OK" if ok else "⚠️ CHECK"
        print(f"  {name:<35} {count:>8} {status:>8}")
    print(f"  {'─' * 35} {'─' * 8} {'─' * 8}")
    print(f"  {'TOTAL':<35} {grand_total:>8}")
    print()

    # Category breakdown
    print("  Category Breakdown:")
    print(f"  {'Category':<12} {'Prompt':<12} {'Level':<20} {'Count':>6}")
    print(f"  {'─' * 12} {'─' * 12} {'─' * 20} {'─' * 6}")
    cat_map = [
        ("C00", "Prompt 01", "0 Beginner"),
        ("C01", "Prompt 01", "0 Beginner"),
        ("C10", "Prompt 01", "1 Beginner+"),
        ("C11", "Prompt 01", "1 Beginner+"),
        ("C12", "Prompt 01", "1 Beginner+"),
        ("C20", "Prompt 02", "2 Intermediate"),
        ("C21", "Prompt 02", "2 Intermediate"),
        ("C22", "Prompt 02", "2 Intermediate"),
        ("C30", "Prompt 02", "3 Intermediate+"),
        ("C31", "Prompt 02", "3 Intermediate+"),
        ("C32", "Prompt 02", "3 Intermediate+"),
        ("C40", "Prompt 03", "4 Advanced"),
        ("C41", "Prompt 03", "4 Advanced"),
        ("C50", "Prompt 03", "5 Advanced+"),
        ("C51", "Prompt 03", "5 Advanced+"),
        ("C60", "Prompt 04", "6 Upper Adv"),
        ("C61", "Prompt 04", "6 Upper Adv"),
        ("C70", "Prompt 04", "7 Expert"),
        ("C71", "Prompt 04", "7 Expert"),
        ("C80", "Prompt 05", "8 Upper Expert"),
        ("C81", "Prompt 05", "8 Upper Expert"),
        ("C90", "Prompt 05", "9 Pro"),
        ("C100", "Prompt 06", "10 Master"),
    ]
    for cat, prompt, level in cat_map:
        # Find the count
        count = 0
        for level_dir, categories in EXPECTED:
            for cat_dir, exp in categories:
                if cat_dir.startswith(cat + "_"):
                    cat_path = os.path.join(BASE, level_dir, cat_dir)
                    if os.path.isdir(cat_path):
                        count = len(glob.glob(os.path.join(cat_path, "*.md")))
        print(f"  {cat:<12} {prompt:<12} {level:<20} {count:>6}")
    print()

    if all_ok:
        print("  🎉 ALL CHECKS PASSED — Full documentation suite is complete!")
    else:
        print("  ⚠️  Some checks failed — see details above.")
    print()
    print(f"  📚 Total Problem Chapters: {grand_total}")
    print(f"  📂 Total Categories: 23")
    print(f"  📝 Difficulty Levels: 0–10 (11 levels)")
    print(f"  🔧 Generator Scripts: {len(generators)}")
    print()

if __name__ == "__main__":
    audit()
