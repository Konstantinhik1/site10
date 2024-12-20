-- Получение списка всех продуктов с сортировкой по имени (по возрастанию) и цене (по возрастанию)
SELECT
    "shopapp_product"."id",
    "shopapp_product"."name",
    "shopapp_product"."description",
    "shopapp_product"."price",
    "shopapp_product"."discount",
    "shopapp_product"."created_at",
    "shopapp_product"."arhived",
    "shopapp_product"."preview"
FROM
    "shopapp_product"
ORDER BY
    "shopapp_product"."name" ASC,
    "shopapp_product"."price" ASC;

-- Получение информации о продукте с ID = 2
SELECT
    "shopapp_product"."id",
    "shopapp_product"."name",
    "shopapp_product"."description",
    "shopapp_product"."price",
    "shopapp_product"."discount",
    "shopapp_product"."created_at",
    "shopapp_product"."arhived",
    "shopapp_product"."preview"
FROM
    "shopapp_product"
WHERE
    "shopapp_product"."id" = 2
LIMIT 21;

-- Получение изображений для продукта с ID = 2
SELECT
    "shopapp_productimage"."id",
    "shopapp_productimage"."product_id",
    "shopapp_productimage"."image",
    "shopapp_productimage"."description"
FROM
    "shopapp_productimage"
WHERE
    "shopapp_productimage"."product_id" IN (2);

SELECT
    "django_session"."session_key",
    "django_session"."session_data",
    "django_session"."expire_date"
FROM
    "django_session"
WHERE
    (
        "django_session"."expire_date" > '2024-12-20 11:31:48.123482'
        AND "django_session"."session_key" = 'ompsefcm7lgw22rebjw0osgfzwf0d8f2'
    )
LIMIT 21;

-- 1. Проверка действительности сессии Django
SELECT
    "django_session"."session_key",
    "django_session"."session_data",
    "django_session"."expire_date"
FROM
    "django_session"
WHERE
    (
        "django_session"."expire_date" > '2024-12-20 11:31:48.123482'
        AND "django_session"."session_key" = 'ompsefcm7lgw22rebjw0osgfzwf0d8f2'
    )
LIMIT 21;

-- 2. Получение информации о пользователе
SELECT
    "auth_user"."id",
    "auth_user"."password",
    "auth_user"."last_login",
    "auth_user"."is_superuser",
    "auth_user"."username",
    "auth_user"."first_name",
    "auth_user"."last_name",
    "auth_user"."email",
    "auth_user"."is_staff",
    "auth_user"."is_active",
    "auth_user"."date_joined"
FROM
    "auth_user"
WHERE
    "auth_user"."id" = 1
LIMIT 21;

-- 3. Получение заказов и пользователей, связанных с заказами
SELECT
    "shopapp_order"."id",
    "shopapp_order"."delivery_address",
    "shopapp_order"."promocode",
    "shopapp_order"."created_at",
    "shopapp_order"."user_id",
    "shopapp_order"."receipt",
    "auth_user"."id",
    "auth_user"."password",
    "auth_user"."last_login",
    "auth_user"."is_superuser",
    "auth_user"."username",
    "auth_user"."first_name",
    "auth_user"."last_name",
    "auth_user"."email",
    "auth_user"."is_staff",
    "auth_user"."is_active",
    "auth_user"."date_joined"
FROM
    "shopapp_order"
INNER JOIN
    "auth_user"
ON
    ("shopapp_order"."user_id" = "auth_user"."id");

-- 4. Получение продуктов, связанных с заказом
SELECT
    ("shopapp_order_products"."order_id") AS "_prefetch_related_val_order_id",
    "shopapp_product"."id",
    "shopapp_product"."name",
    "shopapp_product"."description",
    "shopapp_product"."price",
    "shopapp_product"."discount",
    "shopapp_product"."created_at",
    "shopapp_product"."arhived",
    "shopapp_product"."preview"
FROM
    "shopapp_product"
INNER JOIN
    "shopapp_order_products"
ON
    ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE
    "shopapp_order_products"."order_id" IN (1)
ORDER BY
    "shopapp_product"."name" ASC,
    "shopapp_product"."price" ASC;

-- 1. Проверка действительности сессии Django
SELECT
    "django_session"."session_key",
    "django_session"."session_data",
    "django_session"."expire_date"
FROM
    "django_session"
WHERE
    (
        "django_session"."expire_date" > '2024-12-20 11:42:19.769277'
        AND "django_session"."session_key" = 'ompsefcm7lgw22rebjw0osgfzwf0d8f2'
    )
LIMIT 21;

-- 2. Получение информации о пользователе с ID = 1
SELECT
    "auth_user"."id",
    "auth_user"."password",
    "auth_user"."last_login",
    "auth_user"."is_superuser",
    "auth_user"."username",
    "auth_user"."first_name",
    "auth_user"."last_name",
    "auth_user"."email",
    "auth_user"."is_staff",
    "auth_user"."is_active",
    "auth_user"."date_joined"
FROM
    "auth_user"
WHERE
    "auth_user"."id" = 1
LIMIT 21;

-- 3. Получение всех заказов
SELECT
    "shopapp_order"."id",
    "shopapp_order"."delivery_address",
    "shopapp_order"."promocode",
    "shopapp_order"."created_at",
    "shopapp_order"."user_id",
    "shopapp_order"."receipt"
FROM
    "shopapp_order";

-- 4. Получение продуктов, связанных с заказом с ID = 1
SELECT
    ("shopapp_order_products"."order_id") AS "_prefetch_related_val_order_id",
    "shopapp_product"."id",
    "shopapp_product"."name",
    "shopapp_product"."description",
    "shopapp_product"."price",
    "shopapp_product"."discount",
    "shopapp_product"."created_at",
    "shopapp_product"."arhived",
    "shopapp_product"."preview"
FROM
    "shopapp_product"
INNER JOIN
    "shopapp_order_products"
ON
    ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE
    "shopapp_order_products"."order_id" IN (1)
ORDER BY
    "shopapp_product"."name" ASC,
    "shopapp_product"."price" ASC;

-- 5. Повторное получение информации о пользователе с ID = 1
SELECT
    "auth_user"."id",
    "auth_user"."password",
    "auth_user"."last_login",
    "auth_user"."is_superuser",
    "auth_user"."username",
    "auth_user"."first_name",
    "auth_user"."last_name",
    "auth_user"."email",
    "auth_user"."is_staff",
    "auth_user"."is_active",
    "auth_user"."date_joined"
FROM
    "auth_user"
WHERE
    "auth_user"."id" = 1
LIMIT 21;

-- 1. Проверка действительности сессии Django
SELECT
    "django_session"."session_key",
    "django_session"."session_data",
    "django_session"."expire_date"
FROM
    "django_session"
WHERE
    (
        "django_session"."expire_date" > '2024-12-20 11:52:03.484357'
        AND "django_session"."session_key" = 'ompsefcm7lgw22rebjw0osgfzwf0d8f2'
    )
LIMIT 21;

-- 2. Получение информации о пользователе с ID = 1
SELECT
    "auth_user"."id",
    "auth_user"."password",
    "auth_user"."last_login",
    "auth_user"."is_superuser",
    "auth_user"."username",
    "auth_user"."first_name",
    "auth_user"."last_name",
    "auth_user"."email",
    "auth_user"."is_staff",
    "auth_user"."is_active",
    "auth_user"."date_joined"
FROM
    "auth_user"
WHERE
    "auth_user"."id" = 1
LIMIT 21;

-- 3. Получение всех заказов
SELECT
    "shopapp_order"."id",
    "shopapp_order"."delivery_address",
    "shopapp_order"."promocode",
    "shopapp_order"."created_at",
    "shopapp_order"."user_id",
    "shopapp_order"."receipt"
FROM
    "shopapp_order";

-- 4. Повторное получение информации о пользователе с ID = 1
SELECT
    "auth_user"."id",
    "auth_user"."password",
    "auth_user"."last_login",
    "auth_user"."is_superuser",
    "auth_user"."username",
    "auth_user"."first_name",
    "auth_user"."last_name",
    "auth_user"."email",
    "auth_user"."is_staff",
    "auth_user"."is_active",
    "auth_user"."date_joined"
FROM
    "auth_user"
WHERE
    "auth_user"."id" = 1
LIMIT 21;

-- 5. Получение продуктов, связанных с заказом с ID = 1
SELECT
    "shopapp_product"."id",
    "shopapp_product"."name",
    "shopapp_product"."description",
    "shopapp_product"."price",
    "shopapp_product"."discount",
    "shopapp_product"."created_at",
    "shopapp_product"."arhived",
    "shopapp_product"."preview"
FROM
    "shopapp_product"
INNER JOIN
    "shopapp_order_products"
ON
    ("shopapp_product"."id" = "shopapp_order_products"."product_id")
WHERE
    "shopapp_order_products"."order_id" = 1
ORDER BY
    "shopapp_product"."name" ASC,
    "shopapp_product"."price" ASC;
