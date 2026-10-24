# ============================================
# House Price Prediction — গড় পদ্ধতি
# ============================================

# বাড়ির তথ্য
sizes = [150, 200, 250, 300]
prices = [10000, 20000, 30000, 40000]

# প্রতিটা বাড়ির per sqft দাম
for i in range(len(sizes)):
    price_per_sqft = prices[i] / sizes[i]
    print(f"বাড়ি{i+1}: সাইজ={sizes[i]}, প্রতি স্কেয়ার ফিট ={price_per_sqft:.3f} Taka")

print("\n--- এখন গড় বের করব ---")

# সব per sqft দাম যোগ করি
total = 0
for i in range(len(sizes)):
    total = total + (prices[i] / sizes[i])

# গড় বের করি
average = total / len(sizes)
print(f"গড় প্রতি sqft দাম = {average:.3f} Taka")

# নতুন বাড়ির দাম অনুমান
new_size = 1800
predicted_price = average * new_size
print(f"\n১৮০০ sqft বাড়ির আনুমানিক দাম = {predicted_price:.2f} Taka")