docker stop ds_server && docker rm ds_server
docker build -t hse_ds_server .
docker run --name ds_server -it hse_ds_server
