package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

// Product represents the product model
type Product struct {
	ID    string  `json:"id"`
	Name  string  `json:"name"`
	Price float64 `json:"price"`
}

var products = make(map[string]Product)

func main() {
	router := gin.Default()

	// Test verisi ekle
	products["1"] = Product{ID: "1", Name: "Laptop", Price: 999.99}
	products["2"] = Product{ID: "2", Name: "Phone", Price: 499.99}

	api := router.Group("/api")
	{
		api.POST("/products", createProduct)
		api.GET("/products", getProducts)
	}

	router.Run(":8002")
}

func createProduct(c *gin.Context) {
	var newProduct Product
	if err := c.ShouldBindJSON(&newProduct); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	id := string(len(products) + 1)
	newProduct.ID = id
	products[id] = newProduct

	c.JSON(http.StatusOK, newProduct)
}

func getProducts(c *gin.Context) {
	c.JSON(http.StatusOK, products) // Map direkt olarak dönüyor
} 