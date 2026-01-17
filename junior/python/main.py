from typing import List, Tuple, Dict
import json


def count_vertical_and_horizontal_panels(
    panel_width: int,
    panel_height: int,
    roof_width: int,
    roof_height: int
) -> dict:
    vertical_columns = roof_width // panel_width
    vertical_rows = roof_height // panel_height
    vertical_panels = vertical_columns * vertical_rows

    used_height = vertical_rows * panel_height
    remaining_height = roof_height - used_height

    horizontal_columns = roof_width // panel_height
    horizontal_rows = remaining_height // panel_width
    horizontal_panels = horizontal_columns * horizontal_rows

    return {
        "vertical_panels": vertical_panels,
        "horizontal_panels": horizontal_panels,
        "total_panels": vertical_panels + horizontal_panels,
    }


def calculate_panels(panel_width: int, panel_height: int, roof_width: int, roof_height: int) -> int:
    max_roof_area = roof_width * roof_height
    max_panel_area = panel_width * panel_height

    if roof_width < panel_width or roof_height < panel_height:
        return 0

    return max_roof_area // max_panel_area


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")
        print(count_vertical_and_horizontal_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        ))
        print("-------------------\n")

def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
