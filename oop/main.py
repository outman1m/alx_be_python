from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

    # اختبار إضافي (اختياري)
    Calculator.change_calculation_type("Basic Math Ops")
    print("\nAfter changing calculation type:")
    Calculator.multiply(8, 3)

if __name__ == "__main__":
    main()
