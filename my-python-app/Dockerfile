FROM python 
WORKDIR /app
COPY ./requirement.txt .
RUN pip install -r requirement.txt 
#pass -r followed by req.txt file as its not like npm install which automatically finds package.json 
COPY . .
# RUN chmod +x app.py && python3 app.py (this will crash as you are installing te flask and running it at the same time so run it with CMD after built it complete)
EXPOSE 5000
CMD [ "python3", "app.py" ]