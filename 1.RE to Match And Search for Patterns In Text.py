import re
def main():
    text = input("Enter some text: ")
    pattern = r'\b[Aa]\w+'
    matches = re.findall(pattern, text)
    if matches:
      print("Matches found")
      for a in matches:
          print(a)
    else:
        print("No Matches found")
if __name__ == "__main__":
    main()
