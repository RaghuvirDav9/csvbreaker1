Week-1 (Master AWS batch and cludwatch rule) everything should be done via cloudformation file(.yaml) - so that we can reuse
----------------------------------------------------------------------------------------------------------------------------
Using cloudformation create RDS postgres db with minimum resources. USe .sql script to create users for read and write.
Create a batch compute env, queue and the job definition using cloudformation. Create a cloudwatch rule to trigger the batch
job every day at 11 AM and that batch job should write 100 records to RDS instance everyday.



1.run dockerfile to create an image of the code
2.upload it to repository aws ecr or dockerhub(here ecr)
3.update image url in yaml file
4.after running yaml in cloudformation run run.py 
 - it will create users for read and write
 - run.py will execute commands in commands.sql



after that event rule will automatically insert data every 5 min in the rds created by cloudformation.
