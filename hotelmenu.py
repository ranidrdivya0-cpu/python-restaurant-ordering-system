{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ee4dd6fb-5987-4931-833b-fff9c2b07fe9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#define the menu of restaurant \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f36a2b48-5e80-4e5e-b017-b033dfff3361",
   "metadata": {},
   "outputs": [],
   "source": [
    "menu={\n",
    "    'pizza':40,\n",
    "    'pasta':50,\n",
    "    'Burger':60,\n",
    "    'Salad':70,\n",
    "    'Coffee':80,\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9fe92ee5-73fb-4254-bf47-5b4d5cd7e123",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'pizza': 40, 'pasta': 50, 'Burger': 60, 'Salad': 70, 'Coffee': 80}\n"
     ]
    }
   ],
   "source": [
    "print(menu)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "dc79e1c4-5b37-451e-b73a-7547ee3fd66d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# greet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "5c2caccc-f264-44f3-808b-26b1e922061c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Python Restaurant\n",
      "Pizza: Rs.40\n",
      "Pasta: Rs.50\n",
      "Burger: Rs.60\n",
      "Salad: Rs.70\n",
      "Coffee: Rs.80\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the name of item you want to order =  pasta\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your item pasta has been added to your order\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to add another item? (yes/no) =  yes\n",
      "Enter the name of second item =  coffee\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Item coffee has been added to order\n",
      "The total amount of items is Rs. 130\n"
     ]
    }
   ],
   "source": [
    "print(\"Welcome to Python Restaurant\")\n",
    "print(\"Pizza: Rs.40\\nPasta: Rs.50\\nBurger: Rs.60\\nSalad: Rs.70\\nCoffee: Rs.80\")\n",
    "\n",
    "menu = {\n",
    "    \"pizza\": 40,\n",
    "    \"pasta\": 50,\n",
    "    \"burger\": 60,\n",
    "    \"salad\": 70,\n",
    "    \"coffee\": 80\n",
    "}\n",
    "\n",
    "order_total = 0\n",
    "\n",
    "item_1 = input(\"Enter the name of item you want to order = \").lower()\n",
    "\n",
    "if item_1 in menu:\n",
    "    order_total += menu[item_1]\n",
    "    print(f\"Your item {item_1} has been added to your order\")\n",
    "else:\n",
    "    print(f\"Ordered item {item_1} is not available yet!\")\n",
    "\n",
    "another_order = input(\"Do you want to add another item? (yes/no) = \").lower()\n",
    "\n",
    "if another_order == \"yes\":\n",
    "    item_2 = input(\"Enter the name of second item = \").lower()\n",
    "\n",
    "    if item_2 in menu:\n",
    "        order_total += menu[item_2]\n",
    "        print(f\"Item {item_2} has been added to order\")\n",
    "    else:\n",
    "        print(f\"Ordered item {item_2} is not available!\")\n",
    "\n",
    "print(f\"The total amount of items is Rs. {order_total}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "917b7ba4-9a36-4ca6-abe5-3d3d2905a6fc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
