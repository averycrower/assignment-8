from transformers import pipeline

# Load the English to Spanish translation model
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")

# Input paragraph (you can change this to anything you'd like!)
text = """
In a world increasingly governed by data and digital systems, access alone is no longer enough. The right to connect must be 
paired with the right to privacy, autonomy, and protection from exploitation. As cities integrate smart technologies and digital 
infrastructure into every layer of public life, from transportation to policing to education, questions of who benefits and who 
is harmed grow more urgent. While “digital inclusion” is often framed as a matter of closing the access gap, such framings overlook 
the deeper power imbalances embedded in our technological systems. This thesis takes the position that inclusion, without 
transparency or accountability, can easily become another form of control.
"""

# Translate paragraph
translation = translator(text, max_length=400)  # increase max_length for longer text

# Display results
print("Original Paragraph:\n", text.strip())
print("\nTranslated Paragraph:\n", translation[0]['translation_text'])
