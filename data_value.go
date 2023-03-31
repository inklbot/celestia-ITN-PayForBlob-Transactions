package main

import (
	"crypto/rand"
	"encoding/hex"
	"fmt"
)

func main() {
	// generate a random namespace ID
	nID := generateRandHexEncodedNamespaceID()

	// generate a random hex-encoded message
	msg := generateRandMessage(27)

	fmt.Println(fmt.Sprintf("My hex-encoded namespace ID: %s\n\nMy hex-encoded message: %s", nID, msg))
}

func generateRandHexEncodedNamespaceID() string {
	nID := make([]byte, 8)
	_, err := rand.Read(nID)
	if err != nil {
		panic(err)
	}
	return hex.EncodeToString(nID)
}

func generateRandMessage(length int) string {
	msg := make([]byte, length)
	_, err := rand.Read(msg)
	if err != nil {
		panic(err)
	}
	return hex.EncodeToString(msg)
}
