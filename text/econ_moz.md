<head>
    <link rel="stylesheet" href="../styles.css">
</head>

<a href="../index.html" class="button">Back to Main Page</a>

# Topic Modeling

Topic modeling is increadible useful to conduct research on economies with little administrative capacity. This page outlines the great potential to gain novel insights from large amounts of unstructured text, such as the mission statements of entries in the national bulletin of Mozambique, the BDR3 that analyse in my dissertation. Topic modeling is a natural language processing technique that identifies latent thematic patterns within unstructured text data, enabling the extraction of meaningful insights by categorizing documents into topics based on shared semantic content.

To demonstrate how this is useful lets' say we are interested in the formalization of sport clubs and religious communities in Mozambique over time. Needless to say, the public authorities in Mozambique to not publish such statistics. The only thing that is aviable are the entries of the BDR3 which contains mission statments for every company or association that get formalized with a publication in the bulletin.

The time series below shows the number of annually registered associations in the BDR3 that mention one of these three topics in their mission statement. The plot shows on an individual level two trends: First  the number of annually registered sports clubs and christian communities increased over the last two decades. In contrast, remains the formalization of muslim faith communities at  lower level throughout the same period. The National Statistics Institute estimated that around 20% of Mozambican citizens are Muslims, suggesting that a large disparities in terms of institutionalized among the coutnries religous communities. This helps to understand the underlying social dynmaics of the ongoing islamist insurgency in northern Mozambique [(more information)](https://www.crisisgroup.org/africa/east-and-southern-africa/mozambique). As next step, we could identify the board members of each association or geocode their headquarters.

<img class="markdown-image" src="../assets/bert_topics/football_christian_muslim.png" alt="football_christian_muslim.png">

## How Topic Modelling works

The beatuy of Topic modeling is that it does not require any presumptions which topics are relevant in the data. If we would use keywords to classify the topics in the BDR3 entries, we'll ingore any information that is not captured by the keywords we select. Without analyzing at the BDR3 data, no one knows the full set of assocations that register in Mozambique, definining the keywords to cluster these entities remains therfore an  educated guess. In contrast. this unsupervised ML algorithm structures the text corpus as whole - which allows to oberserve all information at one glance.

Expalining all technical details of this approach is beyond the scope of this overview. If you want learn more about the algorithm ,  I recommand the excellent  documentation of [BERTtopic](https://arxiv.org/abs/2203.05794), the class-based TF-IDF procedure  that I use.  At a very high level the data pipeline consists of 6 sequential steps:

1. Auto-translation of the mission statements from Portuguese to English.
2. Embedding documents.
3. Reducing embeddings in dimensionality.
4. Cluster embeddings.
5. Tokenize documents per cluster.
6. Extract the best representing of words per topic by weighting them (tf-idf)

It is computational not really feasible cluster all mission statements directly with a Large Language Model (LLM). However, suitable extension to this pipeline would be to use an LLM to summarize and describe each topic representation.

We can visualize the distance between topics in a two dimensional representation. This shows differences and similarities among the word vectors that represent the mission statements in the BD3. The following interactive figure
shows the topics of the mission statements of  associations (associacao) that I use in the time series above to to compare the formalization of sports clubs and religious communities over time.

<iframe src= "../assets/bert_topics/intertopic_distance/associacao_topic.html" width="100%" height="800px"></iframe>

You can click on the  headlines  below to view the 2-D topic distance representation of businesses that te registered in the BD3.

<details> 
<summary> Individual Company (sociedade individual) </summary>
<br>
<iframe src="../assets/bert_topics/intertopic_distance/sociedade_individual_topic.html" width="100%" height="800px"></iframe>
</details>

<details> 
<summary> Private Limited Company (sociedade por quotas) </summary>
<br>
<iframe src="../assets/bert_topics/intertopic_distance/sociedade_por_quotas_topic.html" width="100%" height="800px"></iframe>
</details>

---

# Supplementing Topic Modelling with Trade Data

If we link the sentiment of registered firms to national trade statistics, we gain additional insights. In this example, we look at the import of fertilizer into Mozambique, as measured by the BACI trade dataset. BACI builds upon the United Nations Commodity Trade Statistics Database (UN Comtrade) and cross-validates bilateral import and export statistics. The figure below plots the imports of fertilizer with a line chart. The histogram lists the numbers of annually registered companies that trade or produce fertilizer according to their mission statement in Mozambique between 1985 and 2021.

The figure shows that fertilizer imports skyrocketed in 2008, while the number of domestic companies that trade with fertilizer remained relatively stable before 2010. After 2010, the number of companies that trade with fertilizer increased, but the imports of fertilizer decreased to the initial import level.

<img class="markdown-image" src="../assets/baci_bdr/fertilizer.jpg" alt="fertilizer.jpg">

---

# Improving Macroeconomic Models

Sentiment analysis of the bulletin provides not only micro-level insights but also allows us to build better macroeconomic models. The best existing measure of social activities in the Mozambican economy, to my knowledge, is the Social Accounting Matrix (SAM) of Mozambique. The SAM is composed by the United Nations University World Institute for Development Economics Research (UNU-WIDER). It is a static macro overview that provides a detailed representation of the Mozambican economy and separates 55 activities and commodities in 2015. It uses data from the IMF as well as national accounts to estimate financial flows between different social and economic activities. The network graph of the SAM 2015, the most recent version, has the following shape:

<img class="markdown-image" src="../assets/accounting_matrix/sam_15.jpg" alt="sam_15.jpg">

To study this economy on a firm level, we can also consider Orbis, a corporate business intelligence database. The quality of Orbis data is very heterogeneous across countries. For Mozambique, the database lists around 15,000 operating entities. The bar chart segregates these companies by sector.

<img class="markdown-image" src="../assets/orbis_moz/barh_orbis.jpg" alt="barh_orbis.jpg">
