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
        text description
    }

    Product {
        int id
        string name
        text description
        decimal price
        string image
        int stock
        bool is_active
        datetime created_at
        int category_id  -- FK to Category
    }

    Order {
        int id
        int user_id      -- FK to User
        bool is_paid
        decimal total_price
        datetime created_at
    }

    OrderItem {
        int id
        int order_id     -- FK to Order
        int product_id   -- FK to Product
        int quantity
        decimal price
    }

````