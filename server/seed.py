#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Recipe, User

fake = Faker()

with app.app_context():
    # Delete all rows in tables
    print("Deleting existing data...")
    Recipe.query.delete()
    User.query.delete()
    
    # Create users
    print("Creating users...")
    user1 = User(
        username='john_doe',
        image_url='https://example.com/john.jpg',
        bio='Love cooking Italian food!'
    )
    user1.password_hash = 'password123'
    
    user2 = User(
        username='jane_smith',
        image_url='https://example.com/jane.jpg',
        bio='Passionate about baking and desserts.'
    )
    user2.password_hash = 'password456'
    
    db.session.add_all([user1, user2])
    db.session.commit()
    
    # Create recipes
    print("Creating recipes...")
    recipe1 = Recipe(
        title='Spaghetti Carbonara',
        instructions='Cook spaghetti according to package directions. In a bowl, whisk eggs and parmesan. Cook pancetta until crispy. Toss hot pasta with pancetta, then remove from heat and quickly stir in egg mixture. Season with black pepper and serve immediately.',
        minutes_to_complete=30,
        user_id=user1.id
    )
    
    recipe2 = Recipe(
        title='Chocolate Chip Cookies',
        instructions='Preheat oven to 375°F. Cream together butter and sugars. Beat in eggs and vanilla. Mix in flour, baking soda, and salt. Fold in chocolate chips. Drop spoonfuls onto baking sheet. Bake for 10-12 minutes until golden brown. Cool on wire rack.',
        minutes_to_complete=25,
        user_id=user2.id
    )
    
    recipe3 = Recipe(
        title='Caesar Salad',
        instructions='Make dressing by combining mayo, lemon juice, garlic, worcestershire, and anchovy paste. Toss romaine lettuce with dressing. Add croutons and parmesan cheese. Top with grilled chicken if desired. Season with black pepper and serve immediately.',
        minutes_to_complete=15,
        user_id=user1.id
    )
    
    db.session.add_all([recipe1, recipe2, recipe3])
    db.session.commit()
    
    print("Database seeded successfully!")