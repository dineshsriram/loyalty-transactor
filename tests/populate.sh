echo -e "Create User"
curl -d '{"firstName":"Dinesh", "lastName": "Sriram", "email": "dinesh@test1.com"}' -H "Content-Type: application/json" -X POST http://localhost:5000/user

echo -e "\n\nGet All Users"
curl -d '{}' -H "Content-Type: application/json" -X GET http://localhost:5000/user

echo -e "\n\nRetrieve User"
curl -d '{}' -H "Content-Type: application/json" -X GET http://localhost:5000/user/1

echo -e "\nAdd Transfers\n"
echo -e "Add 50 points\n"
curl -d '{"points":50, "userId":1}' -H "Content-Type: application/json" -X PUT http://localhost:5000/transfer
echo -e "\n\nDeduct 50 points\n"
curl -d '{"points":-50, "userId":1}' -H "Content-Type: application/json" -X PUT http://localhost:5000/transfer

echo -e "\n\nGet All transfers for user\n"
curl -d '{}' -H "Content-Type: application/json" -X GET http://localhost:5000/transfer/1
