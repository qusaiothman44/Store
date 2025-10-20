# Store
```mermaid
erDiagram

    auth_user ||--o{ Order : has
    Order ||--|{ OrderItem : contains
    Product ||--o{ OrderItem : appears_in
    Category ||--o{ Product : contains

    auth_user {
        int id
        string username
        string email
    }

    Category {
        int id
        string name
        string description
    }

    Product {
        int id
        string name
        string description
        float price
        string image
        int stock
        boolean is_active
        datetime created_at
        int category_id
    }

    Order {
        int id
        int user_id
        boolean is_paid
        float total_price
        datetime created_at
    }

    OrderItem {
        int id
        int order_id
        int product_id
        int quantity
        float price
    }

````