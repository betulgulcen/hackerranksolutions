English = int(input())
EnglishNumbers = set(map(int, input().split()))

French = int(input())
FrenchNumbers = set(map(int, input().split()))

print(len(EnglishNumbers.difference(FrenchNumbers)))
