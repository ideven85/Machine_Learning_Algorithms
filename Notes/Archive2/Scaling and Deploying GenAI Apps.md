# Scaling and Deploying GenAI Apps  
# Scaling and Deploying GenAI Apps  
  
## Introduction to Cloud Computing Part 1  
## Introduction to Cloud Computing Part 1  
   
   
  
In the upcoming sessions, you will understand the evolution of the cloud. You will understand what cloud computing is, the different technologies that made cloud computing possible and how it solved the problems faced before its advent. Then, you will learn about various deployment and service models and explore their essential characteristics. After this, you will learn about the benefits of cloud computing by exploring its advantages over on-premises data centres.  
In the upcoming sessions, you will understand the evolution of the cloud. You will understand what cloud computing is, the different technologies that made cloud computing possible and how it solved the problems faced before its advent. Then, you will learn about various deployment and service models and explore their essential characteristics. After this, you will learn about the benefits of cloud computing by exploring its advantages over on-premises data centres.  
  
   
   
  
You will be able to gain fundamental knowledge and practical skills required to build and deliver solutions on the cloud using the services of a major public cloud service provider, Amazon Web Services (AWS).  You will also get hands-on experience in using the storage, computing, and networking services within the AWS environment. boto3 aws. python. aws lambda  
You will be able to gain fundamental knowledge and practical skills required to build and deliver solutions on the cloud using the services of a major public cloud service provider, Amazon Web Services (AWS).  You will also get hands-on experience in using the storage, computing, and networking services within the AWS environment. boto3 aws. python. aws lambda  
  
   
   
  
In this session  
In this session  
  
This session will focus on the role of computing environments and their different types. Then, you will be able to understand what cloud computing is and how it solved the problems faced before its advent. Next, you will learn in detail about the fundamental technologies that made cloud computing possible and the various architectures and deployment models prevelant in the industry today.  
This session will focus on the role of computing environments and their different types. Then, you will be able to understand what cloud computing is and how it solved the problems faced before its advent. Next, you will learn in detail about the fundamental technologies that made cloud computing possible and the various architectures and deployment models prevelant in the industry today.  
  
   
   
  
The broad topics covered in this session are as follows:  
The broad topics covered in this session are as follows:  
* Introduction to cloud computing  
* Introduction to cloud computing  
* Benefits of the cloud  
* Benefits of the cloud  
* Fundamental technologies of the cloud  
* Fundamental technologies of the cloud  
* Cloud deployment models  
* Cloud deployment models  
* Cloud service models  
* Cloud service models  
  
  
## Introduction to Cloud Computing Part 2  
## Introduction to Cloud Computing Part 2  
  
  
# Introduction to Cloud Computing and its Benefits  
# Introduction to Cloud Computing and its Benefits  
  
### Transcript  
### Transcript  
  
So in this segment, we'll try to 1st understand what is cloud computing, then we'll talk about AWS.So AWS is not was not always in the same shape how it is today, right?It all started with the small companies with a different vision and a mission and see today how it has evolved into the AWS thing.So we'll try to see the journey.We'll also try to see what are some of the most popular cloud based applications.We'll try to dissect that and let's try to understand what this word cloud computing is.I think cloud has become a buzzword these days.Everyone is talking about cloud and moving on to the cloud.So what this cloud computing in itself is in a very simple nutshell, if I have to explain when to deliver any kind of service to you, I don't have to use any kind of, you know, software to be installed on your system.If I can provide you a service over the Internet itself, that is what known as a cloud computing.Very simple example.I think most of you must be using a e-mail, for example, Gmail service, right?To use a Gmail service, you don't need to install any software.The only thing that you need to do is that have a Internet connection, have a browser open dot Google Gov WWW dot youknowgmail.com and you will do access your e-mail account.And this is what the cloud computing is all about.You can access the Google Gmail application over the Internet for which you don't need any additional infrastructure.So in a nutshell, this is all about cloud computing is So let's try to deep dive into this cloud computing terminologies.So first of all, because these days, because the Internet right, the market has become very diverse.Now, whatever the application that you create here is not only mean for one market, but because it is based over the Internet, it has a global reach.For very example, you know the Facebook started by the Mark Zuckerberg in a close group of the friends and but soon as and when it got famous it moves out of his friends circle to the university, then university to the city, then to the country and now Facebook is everywhere.The only reason the Facebook was able to make its scale to the whole world was because of the cloud computing.The second thing the cloud computing brings into the picture is that you don't have to pay anything upfront.It's just like you are renting a house.When you rent a house, you have to give the payment every month, right?You don't have to pay, you know, the huge amount of money at the start, the self contrary to it.If you buy a house, you have to do it in the beginning itself.Similarly, in a cloud computing, you don't have to pay for the charge of a complete server or the whole infrastructure.It's a pay as you go model in which the more and more you use it, the more you will have to pay in the installments.The third one is that for end user as far as this cloud computing is concerned, they do not have to worry about how the things are put into the place.For end user, the services are being provided to them over the Internet directly into the comfort of that the place where they are living in.The only thing they need to leverage the services provided by this cloud computing platforms is Internet connection.  
  
00:03:14 - 00:06:04  
  
**Evolution and Features of AWS**  
  
The 4th 1 is about the business management users, right.So because of the cloud computing again the everything that you do doesn't have to be you know rely on a on A1 given infrastructure that is running on a particular machine.Rather it is Co located and it can be accessed by the anyone anytime.So it leads to a better management and a better availability as it is available over the Internet.Now let's try to see about how the whole AWS came into the picture, how it all evolved and what was the journey behind it.And let's try to understand the rationale behind it, how this AWS came into the picture.So the story started way back with something called merchant.com, right?So the Amazon started their own first website that was named merchant.com, which was a kind of a website for selling few items.Now what happened in that case was that in order to unify that development efforts, they created a centralized development platform in which all the things that were needed to build the applications, they tried to build some wrappers out of it.They exposed that as a services to all the internal teams that was working on that particular product.Later on, what they felt was that, you know, as that as at that time the service oriented architecture was at boom, people were talking about, you know, the systems talking to each other in the forms of the services and the APIs.What they did was that on the top of the centralized development platform, they started exposing each of them in the terms of the APIs, in the terms of API so that everyone can decouple themselves from this centralized development platform.They can start using this API and, you know, make the process of development quite simple and easy.While they were doing all these things, they realized that if that can work for them, if that thing can work for the Amazon themselves, why don't they do it for the other companies as well?And they saw a lot of market potential in this idea because many of the companies at that time who were, you know, a very low scalar were just getting started, was facing problems in managing their own cloud and infrastructure.So the basic idea was that if it works for them, why it cannot work for the others as well.And that is how it was the whole inception of AWS and with all the basic initial features which they develop for themselves like the centralized development platform and then the APIs on the top of it, it will lead to the launch of AWS with the initial features and then said that that's the time and now AWS has been pitching more and more features into it.And the next addition to that was launch of EC2 instances in the case of the AWS and these are if you see, if you go and see the monthly releases of AWS, every month you will find more and more releases coming into the plane.The things that work for them, what they try to do is that make it work for everyone.  
  
00:06:04 - 00:09:06  
  
**Netflix's Transition to Cloud with AWS**  
  
And this is how today the AWS is so famous, you know, as per one of the number like more than 60% of the company, mostly in the range of the startups are right now powered by AWS, right?And as a result of this, AWS has become one of the biggest contributor in the cloud space.Now this was in the whatever we discussed in the previous slide was from the context of a cloud service provider, right?How they came to the state and how they are helping other companies to grow.But let's try to understand from the purse of a company which was not initially on the cloud and how using the cloud has helped them scale up many, many times.So take for example Netflix.Netflix is a very common company these days and we all are habituated to watching, no, not watching, but binge watching the movies on the Netflix, right?So let's try to see how the Netflix scale with AWS.So initially, when the Netflix was not on the cloud, they used to create their own content and they used to create DVD's out of it, right?And they used to rent or sell this DVD to their customers.If the model was working great because it was on that time when we also used to, you know, watch tape recorders, we used to watch DVD's, series.So that era was about the series and DVD's.But what happened was that the delivery of this DVD's was halted for few days.And, you know, a halt of three days in the sale of the DVD's, you know, resulted in a major, you know, bottleneck in the terms of their sale.Their sale number went down very abruptly and what the people at the network that time realized that this model of renting out the DVDs by the mail is not something very scalable.They wanted to, you know, move in some another directions in the cloud based solution so that you know, sending out this information to the users, right?Sending out these kind of you know whatever the release that they make in the terms of the movies or the creations shouldn't be dependent on the manual intervention or the manual way of sending it from the one people to another.Let's try to automate thing.And that is how they decided about moving on to AWS.What they did was that all that data which were they initially writing on the DVD and then selling it in offline to the customer that tried to move it to the AWS.And that is how the netflix.com came into the picture.Now instead of selling the DVD's, it is available as a cloud application.So anyone, any person living in any corner of the world, they don't have to wait for the DVD to come to their house.Rather, they can just open the Netflix application in any browser of their choice, just with the help of few clicks and the Internet connections and they are ready to go.They just have to pay for the movie Oregon, the you know, Netflix subscription and they're good to go.And this resulted in more than 100 folds growth for the Netflix.Initially it was always challenged by the distance.It was always challenged by the manual intervention.But now moving on to the cloud, they it gave them a new wings.So this is how you know, this is just an example of Netflix.So now let's talk something about few cloud based applications.  
  
00:09:06 - 00:10:31  
  
**Popular Cloud-Based Applications and Service Providers**  
  
As I already mentioned in our previous slide, I took the example of Gmail, but that's not the case.There's so many cloud based application right now.One of the most famous is Facebook, without which we cannot think of a day these days without Facebook.So Facebook is one another very famous cloud based application.Then we have something called Twitter and LinkedIn of course, right?If you're looking for any professional jobs, LinkedIn is also available over the cloud.We have something called Skype, we have Dropbox, we have Google Mail, we have Google Docs.Again, a great way to share your data with the others.You have YouTube, you have Alexa, you have Google Assistant, you have Siri.So there's so many cloud based application which are available right now in the market.So now we have seen what our cloud based application has been, let's try to talk more about cloud service providers.What are the different cloud platforms available and what are the leading market players in that?So in the terms of cloud platforms, the leading player is Immersion Web services as you better know is that AWS.Then we have something called Microsoft Azure which is again competing very happy with the Azure these days and then we have Google Cloud Platform as well.Google is also not very far behind in this race.And if you have to say, I think these are the top three players as of now in the cloud platform.There are so many others also like Oracle have also few of its solutions but these are the leading players in the cloud platforms.  
As I already mentioned in our previous slide, I took the example of Gmail, but that's not the case.There's so many cloud based application right now.One of the most famous is Facebook, without which we cannot think of a day these days without Facebook.So Facebook is one another very famous cloud based application.Then we have something called Twitter and LinkedIn of course, right?If you're looking for any professional jobs, LinkedIn is also available over the cloud.We have something called Skype, we have Dropbox, we have Google Mail, we have Google Docs.Again, a great way to share your data with the others.You have YouTube, you have Alexa, you have Google Assistant, you have Siri.So there's so many cloud based application which are available right now in the market.So now we have seen what our cloud based application has been, let's try to talk more about cloud service providers.What are the different cloud platforms available and what are the leading market players in that?So in the terms of cloud platforms, the leading player is Immersion Web services as you better know is that AWS.Then we have something called Microsoft Azure which is again competing very happy with the Azure these days and then we have Google Cloud Platform as well.Google is also not very far behind in this race.And if you have to say, I think these are the top three players as of now in the cloud platform.There are so many others also like Oracle have also few of its solutions but these are the leading players in the cloud platforms.  
  
### Overview  
### Overview  
  
Cloud computing refers to the delivery of services such as processing, storage, databases, networking, etc. to users and organisations based on their requirement, over the Internet. The servers on which these softwares and databases run are located in data centres across the world. Users and organisations can access these servers through the Internet from anywhere.  
  
Cloud computing is a pay-as-you-go service, i.e., the users pay only for the services that they use.  
  
   
  
The two main users of Cloud are:  
The two main users of Cloud are:  
* **End Users:** These users use cloud services for proprietary benefits.  
* **End Users:** These users use cloud services for proprietary benefits.  
* **Business Management Users:** These users utilise cloud services on an organisational level.  
  
*    
*    
  
The three major cloud providers are:  
The three major cloud providers are:  
* Amazon Web Service (AWS)  
* Amazon Web Service (AWS)  
* Microsoft Azure  
* Microsoft Azure  
* Google Cloud Platform  
* Google Cloud Platform  
  
**Additional Reading**  
**Additional Reading**  
* ++[How AWS evolved](https://aws.amazon.com/blogs/enterprise-strategy/the-fast-and-the-furious-how-the-evolution-of-cloud-computing-is-accelerating-builder-velocity/)++ - This article shows how the evolution of cloud computing accelerated the growth of AWS.  
* ++[How AWS evolved](https://aws.amazon.com/blogs/enterprise-strategy/the-fast-and-the-furious-how-the-evolution-of-cloud-computing-is-accelerating-builder-velocity/)++ - This article shows how the evolution of cloud computing accelerated the growth of AWS.  
* ++[Real-world cloud computing examples](https://www.maropost.com/5-real-world-examples-of-cloud-computing/)++ - This article tells about the top five real-world examples which use cloud computing.  
* ++[Real-world cloud computing examples](https://www.maropost.com/5-real-world-examples-of-cloud-computing/)++ - This article tells about the top five real-world examples which use cloud computing.  
* ++[Open-source Cloud Platforms](https://computingforgeeks.com/top-open-source-cloud-platforms-and-solutions/)++ - This article can tell you about some top open-source cloud platforms.  
* ++[Open-source Cloud Platforms](https://computingforgeeks.com/top-open-source-cloud-platforms-and-solutions/)++ - This article can tell you about some top open-source cloud platforms.  
  
## Benefits of Cloud Computing    
## Benefits of Cloud Computing    
In the previous segment, you learnt about cloud computing and its various applications, and how industries are willing to shift towards the cloud. The cloud is a shared computing environment where you can dynamically **create**, **access**, and **remove** virtual computing resources. It is an implementation of the idea of accessing virtual computing resources remotely. Specifically, cloud computing is the **delivery of computing resources**, including servers, storage, databases, networking, and software** over the internet**.  
  
   
  
In this segment,  you will learn the benefits that cloud infrastructure offers to organisations.  
In this segment,  you will learn the benefits that cloud infrastructure offers to organisations.  
  
In this video, our industry expert will talk about the advantages of using the cloud over an on-premise system.  
In this video, our industry expert will talk about the advantages of using the cloud over an on-premise system.  
  
  
Let's summarise the benefits of using the cloud over traditional data centres-  
Let's summarise the benefits of using the cloud over traditional data centres-  
  
* **Cost Saving:** Cloud computing eliminates the need for buying or maintaining hardware and software resources and for setting up data centres. It also eliminates the need for maintaining computing infrastructure. Most of the cloud services are pay-as-you-go, which means customers only pay for the services that they use. Use of the cloud also reduces the cost associated with staff wages.  
* **Cost Saving:** Cloud computing eliminates the need for buying or maintaining hardware and software resources and for setting up data centres. It also eliminates the need for maintaining computing infrastructure. Most of the cloud services are pay-as-you-go, which means customers only pay for the services that they use. Use of the cloud also reduces the cost associated with staff wages.  
* **Scalability:** Cloud computing provides businesses with the ability to expand their resources when needed. Organisations need not worry about installing infrastructure, as it is done by the cloud service providers. They can also scale up their applications as per requirement.  
* **Scalability:** Cloud computing provides businesses with the ability to expand their resources when needed. Organisations need not worry about installing infrastructure, as it is done by the cloud service providers. They can also scale up their applications as per requirement.  
* **Availability:** Cloud is available at different locations across the world. It allows companies to expand to new geographical regions and deploy the resources globally.  
* **Availability:** Cloud is available at different locations across the world. It allows companies to expand to new geographical regions and deploy the resources globally.  
* **Security: **Cloud allows access to data and applications to authorised and authenticated users only.  
* **Security: **Cloud allows access to data and applications to authorised and authenticated users only.  
* **Data Storage Space:** Organisations can opt for the exact amount of storage they need and pay only for the space that they use.  
  
*    
  
* The image below depicts some of the basic differences between on-premises computing and cloud computing.:  
* The image below depicts some of the basic differences between on-premises computing and cloud computing.:  
  
   
  
[ON-PREMISES](Attachments/118C8EAD-EE63-4B17-9B1D-C6719A7865EC.png)  
  
    
  
**Additional Reading**  
**Additional Reading**  
* ++[Comparison Between On-Premise Systems and Cloud](https://www.softwareadvice.com/resources/cloud-erp-vs-on-premise/)++ -  This article will give you an idea about the differences between cloud and on-premise systems.  
* ++[Comparison Between On-Premise Systems and Cloud](https://www.softwareadvice.com/resources/cloud-erp-vs-on-premise/)++ -  This article will give you an idea about the differences between cloud and on-premise systems.  
  
  
  
  
  
  
##      
##      
Imagine you are working at AWS and it is your job to identify the essential components of AWS as a cloud service provider that will bind every technology on it and also enable a seems experience for the customers.  
  
   
  
Can you try guessing, what all services should one think of? Okay, let’s make this simple for you and go  step-by-step. Firstly, to provide the cloud services you will need a physical infrastructure. This could be called the data center for your technology. Secondly, the physical infrastructure that you set up will have to be accessed by other users through a seamless technology, so the internet would do just that. Now, after creating a platform, you should add the computing resources that users will eventually access virtually for their needs. So a virtual computing resource will be required.  
  
   
  
In the previous segments, you learned that cloud computing is defined as the delivery of computing resources over the internet. Now, it’s time for you to understand the fundamental technologies that brought cloud computing to life. Let’s understand this in detail, by watching the next video.  
In the previous segments, you learned that cloud computing is defined as the delivery of computing resources over the internet. Now, it’s time for you to understand the fundamental technologies that brought cloud computing to life. Let’s understand this in detail, by watching the next video.  
  
To deliver computing resources over the internet, cloud platforms need the following three main ingredients:  
To deliver computing resources over the internet, cloud platforms need the following three main ingredients:  
* **Data center**, i.e., physical infrastructure,  
* **Data center**, i.e., physical infrastructure,  
* **Internet technology** to connect data center resources to the internet, and,  
* **Internet technology** to connect data center resources to the internet, and,  
* **Virtualization technology**, i.e., software to create virtual computing resources.  
  
*    
  
* The term data center refers to the **physical infrastructure** used to manage the IT operations of one organization and includes data storage, processing, distribution, and access. A data center has these three main elements:  
* The term data center refers to the **physical infrastructure** used to manage the IT operations of one organization and includes data storage, processing, distribution, and access. A data center has these three main elements:  
* **Core components**,  
* **Core components**,  
* **Support infrastructure**, and,  
* **Support infrastructure**, and,  
* **Operations staff  **  
* **Operations staff  **  
* [Software](Attachments/3AF9C068-2836-4C75-805F-79401E9265E3.png)  
  
*    Let’s first learn about the **core components** of a data center, then we will learn about the support infrastructure and operations staff.    The core components of a data center are its physical computing resources. They are needed for processing data, storing data, and distributing data. Data centers house multiple physical  
*    Let’s first learn about the **core components** of a data center, then we will learn about the support infrastructure and operations staff.    The core components of a data center are its physical computing resources. They are needed for processing data, storing data, and distributing data. Data centers house multiple physical  
* **Servers **that provide computing power,  
* **Servers **that provide computing power,  
* **Storage devices** for storing data, and  
* **Storage devices** for storing data, and  
* **Network equipment** for connecting the individual servers and storage devices.  
* **Network equipment** for connecting the individual servers and storage devices.  
  
  
  
  
  
   
   
1. **Data center: ** Refers to the physical infrastructure used to manage the IT operations of one organization and includes data storage, processing, distribution, and access. A data center has these three main elements:  
2. **Data center: ** Refers to the physical infrastructure used to manage the IT operations of one organization and includes data storage, processing, distribution, and access. A data center has these three main elements:  
* **Core components**,  
* **Core components**,  
* **Support infrastructure**, and,  
* **Support infrastructure**, and,  
* **Operations staff  - **Core Components  
* **Operations staff  - **Core Components  
  
  
Let’s first learn about the **core components** of a data center, then we will learn about the support infrastructure and operations staff.    The core components of a data center are its physical computing resources. They are needed for processing data, storing data, and distributing data. Data centers house multiple physical  
Let’s first learn about the **core components** of a data center, then we will learn about the support infrastructure and operations staff.    The core components of a data center are its physical computing resources. They are needed for processing data, storing data, and distributing data. Data centers house multiple physical  
* **Servers **that provide computing power,  
* **Servers **that provide computing power,  
* **Storage devices** for storing data, and  
* **Storage devices** for storing data, and  
* **Network equipment** for connecting the individual servers and storage devices.  
* **Network equipment** for connecting the individual servers and storage devices.  
  
  
  
### Network Devices  
### Network Devices  
  
In a data center, servers are housed in multiple **racks **or **cabinets** and are connected to form a network by devices known as **switches**.  
  
 Different types of network topologies or different ways to form a computer network exist. In a typical data center, there are multiple racks, each of which houses various servers.  
  
One popular option is the multitiered model consisting of  
One popular option is the multitiered model consisting of  
* **Top-of-rack switches** that connect rack servers,   
* **Top-of-rack switches** that connect rack servers,   
* **Aggregation switches** that connect top-of-rack switches so that servers in different racks can communicate with each other, and  
* **Aggregation switches** that connect top-of-rack switches so that servers in different racks can communicate with each other, and  
* **Core switches** that connect aggregation switches to the internet.    
* **Core switches** that connect aggregation switches to the internet.    
* [Internet](Attachments/991374DC-378D-4F2C-8289-D281EB2CD611.png)  
* [Internet](Attachments/991374DC-378D-4F2C-8289-D281EB2CD611.png)  
  
  
  
## Data Centers Part 3  
## Data Centers Part 3  
  
  
  
Data centers are critical infrastructure, and they need to be available at all times. This means that they must have minimal or no service interruptions. This property is called **high availability**. Data center also need to operate continuously, even in the case of network disruptions and must recover quickly in case of failures to continue operations. This property is called **fault tolerance**.  A data center needs **support infrastructure** to ensure high availability and fault tolerance. The support infrastructure includes the following:  
Data centers are critical infrastructure, and they need to be available at all times. This means that they must have minimal or no service interruptions. This property is called **high availability**. Data center also need to operate continuously, even in the case of network disruptions and must recover quickly in case of failures to continue operations. This property is called **fault tolerance**.  A data center needs **support infrastructure** to ensure high availability and fault tolerance. The support infrastructure includes the following:  
* **Redundant power supply**: generators, transformers, and uninterruptible power supplies.  
* **Redundant power supply**: generators, transformers, and uninterruptible power supplies.  
* **Environmental controls**: cooling systems and fire protection.  
* **Environmental controls**: cooling systems and fire protection.  
* **Physical security**: access and authorization controls.  
  
*    
  
* To maintain the core components and the support infrastructure, data centers need a **dedicated team of qualified professionals** to  
* To maintain the core components and the support infrastructure, data centers need a **dedicated team of qualified professionals** to  
* **Monitor** data center operations,   
* **Monitor** data center operations,   
* Ensure core equipment and support infrastructure are **maintained**, and  
* Ensure core equipment and support infrastructure are **maintained**, and  
* **Troubleshoot** the system and rectify faults.  
  
*    
  
* In summary, data centers are critical and complex systems that require  
* In summary, data centers are critical and complex systems that require  
* **Core components** for storage, processing, distributing, and accessing data.  
* **Core components** for storage, processing, distributing, and accessing data.  
* **Support infrastructure** to ensure IT operations run uninterruptedly.   
* **Support infrastructure** to ensure IT operations run uninterruptedly.   
* **Operations staff **for monitoring, maintaining, and troubleshooting the data center.  
  
*    
  
* Take-home message:  
  
*    
  
* ***Running a data center is always an expensive operation.***  
* ***Running a data center is always an expensive operation.***  
  
  
## Data Centers Part 4 Networking  
## Data Centers Part 4 Networking  
  
The internet is a global **computer network** consisting of billions of devices (**end devices**) connected by **communication links** and **communication devices**. By connected, we mean they can exchange digital data formatted as **packets**. A packet is a basic unit of data transferred from an origin to a destination address on the internet. In cloud computing, we use the internet to interact remotely with the computing resources housed in a data center.  
  
   
  
**Protocols** control the transmission of packets across the internet. A protocol is an agreed set of rules that specify the format of the packets that devices send and receive and how they get exchanged between devices.     
  
[TRANSMISSION](Attachments/C1806FB6-85AE-4F25-84B9-074BAB1DCFBF.png)  
  
     
  
The main internet protocols are **TCP/IP (transmission control protocol/internet protocol**). TCP/IP dictates that every connected end device should have an address, known as** IP address**. IP addresses are unique numbers identifying a device connected to a TCP/IP network. For sending data packets through the internet, it must contain the IP addresses of the origin and destination devices.  
  
   
  
There are two IP address versions:  
There are two IP address versions:  
* **IPv4**  
* **IPv4**  
* **IPv6**  
  
*  **IPv4** stands for internet protocol version 4. It consists of 32 bits and is represented using dot-decimal notation consisting of 4 decimal numbers between 0 and 255. An example of an IPv4 address is:    
  
* [IPv4 address in dot-decimal notation](Attachments/8D620413-663D-4545-8DA4-465A563A000D.png)  
  
*   **IPv6 **stands for internet protocol version 6 and is a successor to IPv4. It consists of 128 bits; thus, there can be many more IPv6 addresses than IPv4. Because of this, every device can have a unique IPv6 address as opposed to IPv4, where addresses need to be reused.  An example of IPv6 address is:    
  
* [65b4: 732: 45b7; 0000: 0000: 742c: 03e0: 5345](Attachments/C84F90E3-870C-4509-8FFD-666E5768F01C.png)  
  
*      
  
* TCP/IP distinguishes IP addresses into two types:  
* TCP/IP distinguishes IP addresses into two types:  
* **Public IP addresses** and  
* **Public IP addresses** and  
* **Private IP addresses**.  
  
*    
  
* Public IP addresses can be accessed directly via the internet and are assigned to the personal network router by the internet service provider (ISP). They are used for communicating to the internet outside the personal network.  
  
*    
  
* Private addresses are a range of IP addresses used to form private networks. An example of a private network is the home wifi network. Each device within the same network is assigned a unique private IP address, and if an instrument within a private network sends a packet to a private address, this packet never leaves the private network. Private IP addresses allow devices connected to the same private network to communicate with each other without connecting to the entire internet.  
  
*    
  
* The key difference between private and public IP addresses is what they are connected to. You can connect to the wider internet using the public IP address, but private IP addresses allow you to connect securely to other devices within the same private network.   
  
*    
  
* There are millions of private networks across the world, all of which contain devices assigned private IP addresses within the following range:  
* There are millions of private networks across the world, all of which contain devices assigned private IP addresses within the following range:  
* **Class A**: 10.0.0.0 — 10.255.255.255  
* **Class A**: 10.0.0.0 — 10.255.255.255  
* **Class B**: 172.16.0.0 — 172.31.255.255   
* **Class B**: 172.16.0.0 — 172.31.255.255   
* **Class C**: 192.168.0.0 — 192.168.255.255  
  
*    
  
* Private IP addresses are unique in a particular private network, but two private IP addresses can be the same if they are in different private networks. The public addresses range includes all numbers not reserved for private IP addresses. They are unique in nature.  
  
*    
  
* In order to connect a private network to a public network, **gateways** are required. A gateway is a device that is capable of forwarding packets from a device within a private network to the internet. An example of the gateway is the home wifi router.  
  
*    
  
* Data centers use the TCP/IP protocol to form private networks, where servers and other equipment communicate through IP packets. In addition, TCP/IP connects the data center servers to the internet, and it is possible to connect to one of the servers in the data center remotely.  
  
*    
  
* Cloud data centers use TCP/IP to  
* Cloud data centers use TCP/IP to  
* **Form private networks**, where servers communicate with each other and  
* **Form private networks**, where servers communicate with each other and  
* **Connect** its servers to the **internet**.  
  
*    
  
* In the previous segments, you learned that cloud computing is the delivery of computing resources over the internet. Connecting to one of the physical servers in a data center via the internet is an example of accessing cloud computing resources over the internet. When a physical server is completely dedicated to a particular user, it is known as a **bare-metal server**.  
  
*    
  
* A bare-metal server is not suitable for multi-tenant scenarios, where multiple users share the same physical resources. In order to share the physical resources of a data center among multiple users, another technology is required, called **virtualization**.  
* A bare-metal server is not suitable for multi-tenant scenarios, where multiple users share the same physical resources. In order to share the physical resources of a data center among multiple users, another technology is required, called **virtualization**.  
