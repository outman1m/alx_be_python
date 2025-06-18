class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method that doesn't need class/instance access"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method that can access class attributes"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

    # إضافة إضافية لزيادة الفهم (اختياري)
    @classmethod
    def change_calculation_type(cls, new_type):
        """Class method to modify class state"""
        cls.calculation_type = new_type
