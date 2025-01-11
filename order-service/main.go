package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

// Order represents the order model
type Order struct {
	ID          string   `json:"id"`
	Username    string   `json:"username"`
	Products    []string `json:"products"`
	TotalCost   float64  `json:"total_cost"`
}

var orders = make(map[string]Order)

func main() {
	router := gin.Default()

	// Test verisi ekle
	orders["1"] = Order{
		ID: "1",
		Username: "Harun",
		Products: []string{"Laptop"},
		TotalCost: 999.99,
	}

	api := router.Group("/api")
	{
		api.POST("/orders", createOrder)
		api.GET("/orders", getOrders)
	}

	router.Run(":8003")
}

func createOrder(c *gin.Context) {
	var newOrder Order
	
	if err := c.ShouldBindJSON(&newOrder); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	id := string(len(orders) + 1)
	newOrder.ID = id
	orders[id] = newOrder

	c.JSON(http.StatusOK, gin.H{
		"id": id,
		"order": newOrder,
	})
}

func getOrders(c *gin.Context) {
	c.JSON(http.StatusOK, orders)
} 