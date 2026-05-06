#!/usr/bin/env python
"""
Setup script to initialize the database and create a test dealer account.
Run this after migrations: python setup.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from api.models import DealerProfile

def create_test_dealer():
    """Create a test dealer account for login testing."""
    
    # Create superuser
    if not User.objects.filter(username='admin').exists():
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@porsche-dealer.com',
            password='Admin@123'
        )
        print("✓ Superuser created: admin / Admin@123")
    
    # Create test dealer users
    dealers = [
        {
            'username': 'dealer1',
            'email': 'dealer@porsche-dealer.com',
            'password': 'Dealer@123',
            'first_name': 'John',
            'last_name': 'Smith',
            'dealership_code': 'PS-2024',
            'dealership_name': 'Premium Porsche Dealer NYC'
        },
        {
            'username': 'dealer2',
            'email': 'dealer2@porsche-dealer.com',
            'password': 'Dealer@123',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'dealership_code': 'PS-2025',
            'dealership_name': 'Luxury Porsche Dealer LA'
        }
    ]
    
    for dealer_data in dealers:
        if not User.objects.filter(username=dealer_data['username']).exists():
            user = User.objects.create_user(
                username=dealer_data['username'],
                email=dealer_data['email'],
                password=dealer_data['password'],
                first_name=dealer_data['first_name'],
                last_name=dealer_data['last_name']
            )
            
            DealerProfile.objects.create(
                user=user,
                dealership_code=dealer_data['dealership_code'],
                dealership_name=dealer_data['dealership_name'],
                email=dealer_data['email']
            )
            
            print(f"✓ Dealer created: {dealer_data['username']} / {dealer_data['email']}")
            print(f"  Dealership Code: {dealer_data['dealership_code']}")

if __name__ == '__main__':
    print("Setting up test data...")
    create_test_dealer()
    print("\nTest dealer accounts created!")
    print("\nTest Login Credentials:")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Email: dealer@porsche-dealer.com")
    print("Password: Dealer@123")
    print("Dealership Code: PS-2024")
    print("Verification Code: Any 6 digits (e.g., 123456)")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
