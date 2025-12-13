class MathUtils:
    @staticmethod
    def add(a, b):
        """Static method - no self or cls parameter"""
        return a+b
    
    @staticmethod
    def multiple(a,b):
        return a*b
    
print(MathUtils.add(7, 89))
print(MathUtils.multiple(7, 9))
