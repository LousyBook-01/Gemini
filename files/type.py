import time

def Type(text, type_delay=0.02):
  """
  Animates typing text character by character with a delay.

  Args:
    text: The text to be animated.
    type_delay: The delay between each character (in seconds).
  """
  for char in text:
    print(char, end='', flush=True)
    time.sleep(type_delay)
  print()  # Print a newline after the animation is done

# Example usage
text = "This is a typing animation."
Type(text)

text = "You can adjust the speed of the animation."
Type(text)
