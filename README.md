# Django DRF User Audit Project

This project was created by following the tutorial:  
[**Django & DRF: Automatically Set `created_by` and `updated_by` Fields**](https://malnossi.github.io/blog/django-drf-generic-user/).

## Overview

The goal of this project is to implement a **clean and reusable solution** for automatically tracking:
- The user who **created** a record (`created_by`).
- The user who **last updated** a record (`updated_by`).

This solution leverages **Django Rest Framework (DRF)** features such as:
- `HiddenField` for hiding audit fields from API clients.
- `CurrentUserDefault` to automatically set the currently authenticated user.
- `CreateOnlyDefault` to ensure `created_by` is only set during object creation.

---

## Key Features

- **Audit fields:** `created_by`, `updated_by`, `created_at`, and `updated_at`.
- **Automatic population:** No need to override `perform_create` or `perform_update` in each ViewSet.
- **Reusable mixins:** A base `AuditModelMixin` for models and `AuditSerializerMixin` for serializers.
- **DRY architecture:** Moves business logic to the serialization layer for better consistency and maintainability.

---

## Requirements

- Python 3.10+
- Django 4.2+
- Django Rest Framework (DRF) 3.14+