def fibonacci(n):
    # Baasjuhud
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Rekursiivne juht
    else:
        return fibonacci(n-1) + fibonacci(n-2)
