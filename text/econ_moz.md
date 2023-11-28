
<head>
    <link rel="stylesheet" href="../styles.css">
</head>


# Mapping the Mozambican economy

Every society needs data to study and plan the allocation of its resource. This is a crucial constrain for many low income countries is notorious difficult, as public accounts do not have capacity to provide the necessary data. 
This section outlines for the case of Mozambique, how the use of Natural Language Processing (NLP) and Large Language Models can be used to solve this lack of useful data.

Here we lok at the combination of two data sets. First the entries from the Bulletin of the Republic of Mozambique (Boletim da Republica de Moçambique), an official publication of the Mozambican government that documents firm registrations. Second, the trade statistics from the United Nations Commodity Trade Statistics Database (UN Comtrade). To be specific, we use BACI a cleaner version of the UN Comtrade data set.

To illustrate the potential of this data and the potential of NLP, we will start with two simple questions: Where can one buy fertalizer in Mozambique? And which industries use fertalizer?


## Existing measures 

With existing data, we could answer this question via the 2015 Social Accounting Matrix [(SAM)](https://www.wider.unu.edu/database/2015-social-accounting-matrix-mozambique) of Mozambique, composed by the United Nations University World Institute for Development Economics Research (UNU-WIDER). The SAM is a static macro overview that provides a detailed representation of the Mozambican economy and separates 55 activities and commodities in 2015. One of these activities is fertilizer, the figure below shows the network graph of financial flows in (in million Meticals) between each activities and commodities. If we want to know where to buy fertilizer, we would to look at the firm level data, which is not available in the SAM.
Orbis, a business information database documents in detail the financial flows of firms. However, the quality of Orbis data is very heterogeneous across countries. In Mozambique, Orbis documents around 14000 companies, but its not certain whether this sample provides a representative picture of the economy. The database documents NACE industry codes, for all firms in this sample but little additional information for the majority of entries. The horizontal bar plot displays the numbers of companies in each industry. The figure shows that the majority of firms are in the a"business service sector", but the definition of this sector classification  origins form industrialized countries.


<img class="markdown-image" src="../assets/accounting_matrix/sam_15.jpg" alt="sam_15.jpg">


<img class="markdown-image" src="../assets/orbis_moz/barh_orbis.jpg" alt="barh_orbis.jpg">

## Trade and administrative data complement each other

Let's take a look how trade statistics and administrative records can answer this question.
The figure below shows the imports of fertilizer and numbers of annually registered companies that trade with fertilizer in Mozambique between 1985 and 2021. To determine whether a company operates in this business, I apply NLP for a sentiment analysis of a each companies mission statement. 
 

<img class="markdown-image" src="../assets/baci_bdr/fertilizer.jpg" alt="fertilizer.jpg">

The figure shows that fertilizer imports skyrocketed in 2008, while the number of domestic companies that trade with fertilizer remained relatively stable before 2010. After 2010, the number of companies that trade with fertilizer increased, but the imports of fertilizer decreased to the initial import level. 

 We can now look at the location of the xxx firms that operate in total in the fertilizer business. The figure below shows the location of these firms in Mozambique. The figure shows that the majority of firms are located in the capital Maputo, but there are also firms in the north of the country.

[insert map of fertilizer firms]

[mention the failure of the Zambezi Valley project


## How does the sentiment analysis look like ?


Overview of all topics. Example of the associate/faith example. 


Why  existing industry codes are a bit misleading.


