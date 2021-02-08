# csvbreaker1
Using cloudformation create RDS postgres db with minimum resources. USe .sql script to create users for read and write.
Create a batch compute env, queue and the job definition using cloudformation. Create a cloudwatch rule to trigger the batch
job every day at 11 AM and that batch job should write 100 records to RDS instance everyday.



in yaml file you need to specify subnet for your region
and change image url 
