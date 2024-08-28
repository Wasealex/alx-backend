const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const port = 1245;


const client = redis.createClient();
const hgetAsync = promisify(client.hget).bind(client);
const hsetAsync = promisify(client.hset).bind(client);


const listProducts = [
    { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
    { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
    { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
    { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
    { itemId: 5, itemName: 'Suitcase 1080', price: 1550, initialAvailableQuantity: 0 }
];


const getItemById = (id) => {
    return listProducts.find(product => product.itemId === id);
};


app.get('/list_products', (req, res) => {
    res.json(listProducts);
});


const reserveStockById = async (itemId, stock) => {
    await hsetAsync(`item.${itemId}`, 'reserved', stock);
};


const getCurrentReservedStockById = async (itemId) => {
    const reservedStock = await hgetAsync(`item.${itemId}`, 'reserved');
    return reservedStock ? parseInt(reservedStock) : 0;
};


app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);

    if (!product) {
        return res.json({ status: 'Product not found' });
    }

    const reservedStock = await getCurrentReservedStockById(itemId);
    const currentQuantity = product.initialAvailableQuantity - reservedStock;

    res.json({ ...product, currentQuantity });
});


app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);

    if (!product) {
        return res.json({ status: 'Product not found' });
    }

    const reservedStock = await getCurrentReservedStockById(itemId);
    const currentQuantity = product.initialAvailableQuantity - reservedStock;

    if (currentQuantity <= 0) {
        return res.json({ status: 'Not enough stock available', itemId });
    }

    await reserveStockById(itemId, reservedStock + 1);
    res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
