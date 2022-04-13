Prepair microservice with

set .gitmodule to propper repo
git submodule init
git submodule sync
git submodule update


build microservice with
 
mvn clean package (in root)

mvn spring-boot:run (in microservice)

or

java -jar ().jar (in microservice/target/().jar



Change ports in root/microservice/src/main/resources/application.yml



user handles user database (8070)
underwirter handles generating applications (8071)
account.... (8072)
bank handles bank service (8083)

gateway connects services? (4001)
