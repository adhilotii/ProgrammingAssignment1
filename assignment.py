# Name: Adelina Hilotii
# Course: CS701/GB735, Dr. Yalew
# Date: [Submission date]
# Programming Assignment: 1
# Program Inputs: Dimensions of the room (length, width, height) in feet
# Program Outputs: Total area to be painted (in square feet), amount of primer (in gallons), amount of paint (in gallons)

def main():
    
    '''This program Computes the amount of paint needed one more'''
    # Step 1: Ask the user for the dimensions of the room
    # The three dimensions are length - height - width 

        length=23.3
        height=8
        width=12.9

    # Step 2: Compute the total area of the four walls and ceiling
    # Area of walls = 2 * (length * height + width * height)
        area_walls = 2 * (length * height + width * height)
    # Area of ceiling = length * width
        area_ceiling = length * width
    # Total area = Area of walls + Area of ceiling
        total_area = area_walls + area_ceiling

    # Step 3: Calculate the amount of primer and paint needed
    # Primer coverage = 200 square feet per gallon
        primer_coverage = 200
        peimer_needed = total_area / primer_coverage
    # Paint coverage = 350 square feet per gallon
        paint_coverage = 350
        paint_needed = total_area / paint_coverage

    # Step 4: Output the total area and the amount of primer and paint needed
    # Uncomment the three lines below for the output
    print(f"Total area to be painted: {total_area:.2f} square feet")
    print(f"Amount of primer needed: {primer_needed:.2f} gallons")
    print(f"Amount of paint needed: {paint_needed:.2f} gallons")

if __name__ == "__main__":
    main()
