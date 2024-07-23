import matrix_api
import cfg


fname = "test.txt"

client = matrix_api.MatrixClient(cfg.matrix_username, cfg.matrix_pass, cfg.matrix_device_id)

client.login()

client.upload_file(fname)