    signature_path = 'signature.png'  # Path to the signature image
    signature_image = Image.open(signature_path)
    signature_aspect_ratio = signature_image.width / signature_image.height

    # Define the desired width and calculate height to maintain aspect ratio
    signature_width = 1.5 * inch
    signature_height = signature_width / signature_aspect_ratio

    # Draw the signature image below the "Authorized Signature" label
    pdf.drawImage(
        ImageReader(signature_image), 
        5.5 * inch, 
        3.5 * inch - signature_height - 0.2 * inch,  # Adjusted Y-position to avoid overlap
        width=signature_width, 
        height=signature_height, 
        mask='auto'
    )
