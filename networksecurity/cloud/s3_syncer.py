
import os

class S3Sync:
    def sync_folder_to_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync {folder} {aws_bucket_url} "
        os.system(command)

    def sync_folder_from_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync  {aws_bucket_url} {folder} "
        os.system(command)



if __name__ == "__main__":
    print(os.getcwd())

    folder = "/home/douya1218/Documents/Udemy_MLOps_courses/End_to_End_ML_OPS/networksecurity_ETL_Docker_deployOverAWS_EC2/final_model"
    aws_bucket_url = "s3://ddddouya/final_model/05221240"
    s3sync = S3Sync()
    s3sync.sync_folder_to_s3(folder, aws_bucket_url)


