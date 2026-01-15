'''def addition(a,b):
    return a+b

result= addition(3,4)
print(result)

def username_operation(name):
    print(f"my nmae is {name}")
    print(f"i am {name} .studying in MIT WPU")

username_operation("ved")

def greet(name,location):
    print(f"my nmae is {name}")
    print(f"i live at {location}")
greet("ved","Washington")



def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# Calculator usage
a = 10
b = 5

print("Addition:", add(a, b))
print("Subtraction:", sub(a, b))
print("Multiplication:", mul(a, b))
print("Division:", div(a, b))

============================================================

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

direction = input("enter encode to 'encrypt' or enter 'decode' to decrypt\n").lower()
text = input("enter your text \n").lower()
shift = int(input("enter shift number\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"the encoded text={cipher_text}")

encrypt(original_text=text, shift_amount=shift)


===========================================================

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
direction = input("enter encode to 'encrypt' or enter 'decode' to decrypt\n").lower()
text = input("enter your text \n").lower()
shift = int(input("enter shift number\n"))

def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"the encoded text={cipher_text}")

decrypt(original_text=text, shift_amount=shift)

==============================================================

alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]

direction = input("enter encode to 'encrypt' or enter 'decode' to decrypt\n").lower()
text = input("enter your text \n").lower()
shift = int(input("enter shift number\n"))

def caesar(original_text, shift_amount, direction):
    cipher_text = ""
    for letter in original_text:
        if direction == "encode":
            shifted_position = alphabet.index(letter) + shift_amount
        elif direction == "decode":
            shifted_position = alphabet.index(letter) - shift_amount

        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"the encoded text={cipher_text}")

caesar(original_text=text, shift_amount=shift, direction=direction)

============================================================='''




