package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

// User represents the user model
type User struct {
	ID    string `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}

// Global users map to simulate a database
var users = make(map[string]User)

func main() {
	router := gin.Default()

	// Test verisi ekle
	users["1"] = User{ID: "1", Name: "Harun", Email: "harun@mail.com"}
	users["2"] = User{ID: "2", Name: "Ahmet", Email: "ahmet@mail.com"}

	api := router.Group("/api")
	{
		api.POST("/users", createUser)
		api.GET("/users", getUsers)
	}

	router.Run(":8001")
}

func createUser(c *gin.Context) {
	var newUser User
	
	if err := c.ShouldBindJSON(&newUser); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	id := string(len(users) + 1)
	newUser.ID = id
	users[id] = newUser

	c.JSON(http.StatusOK, newUser)
}

func getUsers(c *gin.Context) {
	c.JSON(http.StatusOK, users)
} 