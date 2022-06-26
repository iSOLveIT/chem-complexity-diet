.. Chemical complexity of Diet documentation master file, created by
   sphinx-quickstart on Sun Jun 26 04:16:50 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. raw:: html

   <h2 style="text-align:center;">Chemical Complexity of Diet</h2>

   <h3>Credits</h3>

**Author:** Albert-László Barabási, Giulia Menichetti and Joseph Loscalzo

**Publisher:** Ontomatica

**Published:** 9th December, 2019

**Editor**: Duodu Randy

---------------

.. sectnum::
   :start: 1
   :suffix: .


.. _chap1:

********************************************
The unmapped chemical complexity of our diet
********************************************

**Our understanding of how diet affects health is limited to 150 key nutritional components that are tracked and catalogued by the USDA and other national databases. Although this knowledge has been transformative for health sciences, helping unveil the role of calories, sugar, fat, vitamins and other nutritional factors in the emergence of common diseases, these nutritional components represent only a small fraction of the more than 26,000 distinct, definable biochemicals present in our food — many of which have documented effects on health but remain unquantified in any systematic fashion across different individual foods. Using new advances, such as machine learning, a high-resolution library of these biochemicals could enable the systematic study of the full biochemical spectrum of our diet, opening new avenues through which to understand the composition of what we eat, and how it affects health and disease.**

The maxim of Jean Anthelme Brillat-Savarin, "*Dites-moi ce que vous mangez et je vais vous dire ce que vous êtes*" — 'you are what you eat'
— remains as pertinent today, in the era of modern medicine, as it did in 1826.
Indeed, the exceptional role of diet in health is well documented by decades of research in nutritional epidemiology,
unveiling the role of nutrients and other dietary factors in cardiovascular disease, obesity, type 2 diabetes mellitus
(T2DM) and other common diseases.
Yet, the bulk of our current understanding of the way food affects health is anchored in the 150 nutritional components
that the USDA and other national databases track in the food supply, and these nutritional components represent
only a tiny subset of the total pool of definable biochemicals in the food supply
(see :ref:`Supplementary Discussion 1 <SD1>`).

The dark matter of nutrition
============================

Consider garlic - a key ingredient of the Mediterranean diet; the USDA quantifies 67 nutritional
components in raw garlic, indicating that this bulbous plant is particularly rich in manganese,
vitamin B6, and selenium. However, a clove of garlic contains more than 2,306 distinct chemical
components — from allicin, an organosulfur compound responsible for the distinct aroma of the
freshly crushed herb, to luteolin, a flavone with protective effects in cardiovascular diseases
— none of which is quantified or tracked by the USDA.
They are, however, listed in FooDB, a database representing the most comprehensive effort to integrate
food composition data from specialized databases and experimental data.
As of August 2019, FooDB records the presence of 26,625 distinct biochemicals in food,
a number that is expected to increase in the near future (see :ref:`Supplementary Discussion 2 <SD2>`).
This exceptional chemical diversity could be viewed as the 'dark matter' of nutrition, as most of
these 26,625 chemicals remain largely invisible to both epidemiological studies, as well as to the
public at large.

Where does this remarkable chemical diversity come from? Living organisms require a large number of
biochemicals to grow and survive in their limited environments, well beyond the nutritional components
that we humans need in our diet. From an evolutionary perspective, plants are characterized by
a particularly rich chemical composition - mainly because they are unable to outrun their predators.
Their defense is occasionally mechanical (for example, through the development of spikes),
but predominantly chemical, exercised through smell, taste and appearance.
These chemical defenses require an extensive secondary metabolism that produces a wide range of flavonoids, terpenoids,
and alkaloids. Polyphenols - a highly studied group of chemicals believed to be responsible for the health
effects of tea and other plants - are the product of that secondary metabolism.
The number of secondary metabolites is estimated to exceed 49,000 compounds, indicating that
the 26,000 chemicals currently assigned to food represent an incomplete assessment of the true complexity
of the ingredients we consume.
| Multiple environmental factors, from light to soil moisture, soil fertility, and soil salinity, can
influence the biosynthesis and accumulation of such secondary metabolites.
Humans and other animals who can hunt for the necessary food sources do not have the ability
to synthesize many molecules our metabolism requires, like ascorbic acid or alpha-linolenic acid,
necessitating a source for these essential nutrients.

Overall, an analysis of USDA and FooDB data confirms that plants as a group have the highest chemical
diversity, with approximately 2,000 chemicals detected in most examples.
Yet, 85% of these chemicals remain unquantified, meaning that while their presence has been detected or
inferred, their concentration in specific food ingredients remains unknown (see :ref:`Supplementary Discussion 2 <SD2>`).
With garlic, for example, FooDB reports the chemical concentration for just 146 chemical components;
the remaining 2,160 chemicals listed in FooDB are not quantified.
We therefore raised the question as to whether the scientific literature contains valuable information
on food composition beyond that currently compiled by food databases.
Indeed, experimental and analytical projects focused on specific foods and foodborne chemicals are published
on a daily basis, and only a small fraction of them inform databases.
To unveil this potentially hidden knowledge we developed a pilot project, FoodMine, that uses natural
language processing to mine the full scientific literature for the purpose of expanding comprehensively
all available scientific data on the biochemical composition of foods.

.. figure:: /_static/media/img/1.png
   :figclass: align-center
   :class: no-scaled-link

   **Fig. 1 | Untracked biochemicals and their health implications**. Animal products contain L-carnitine, choline and choline-contributing compounds. These
   molecules are metabolized by gut bacteria into trimethylamine (TMA), which is converted in the liver to trimethylamine-N-oxide (TMAO), a compound
   linked to coronary events. Garlic, extra-virgin olive oil and red wine, staple ingredients of the Mediterranean diet, reduce the production of TMAO through
   allicin and 3,3-dimethylbutan-1-ol (DMB), compounds that block TMA production by gut bacteria. Of the six biochemical compounds involved in this
   pathway, only one, choline, is tracked in food by the USDA. The other compounds are part of the nutritional ‘dark matter’ (in red).

FoodMine identified 5,676 papers from PubMed that potentially report on chemicals pertaining to
the detailed chemical composition of garlic. After filtering this list using machine learning,
we manually evaluated 299 papers, of which 77 reported 1,426 individual chemical measurements pertaining
to garlic's chemical composition. Our pilot project recovered more unique quantified compounds than
catalogued by the USDA and FooDB together (see :ref:`Supplementary Discussion 3 <SD3>` and :ref:`Supplementary Table 1 <ST1>`).
For example, diallyl disulfide is known to contribute to garlic's smell and taste, and is implicated in
the health benefits of garlic, as well as in garlic allergy.
Although FoodMine found multiple publications reporting on its concentration in garlic,
the current databases do not offer quantified information for the compound.
Furthermore, FoodMine identified information for 170 compounds that were not previously linked to garlic,
either in the USDA or FooDB database (see :ref:`Supplementary Discussion 3 <SD3>`).

Taken together, we find that there is a wealth of exceptionally detailed information about food composition
scattered across multiple literature sources. The current incompleteness in coverage within existing food composition
databases is not due to a lack of interest in these chemicals or lack of efforts to map these chemical
building blocks of food. Rather, it reflects the absence of systematic in-depth efforts to identify and
catalogue the data scattered across multiple scientific communities and literature sources.
As we discuss below, high throughput tools required to scan the scientific literature and to overcome
these limitations have emerged in the past several years. Mobilizing them could set the stage for
an in-depth and systematic understanding of the ways by which our food affects health.

Health implications
===================

The focus on the 150 nutritional components, such as salt, sugar, protein, and fat has been justified,
given the important role each of them plays in health and disease.
Yet, many documented health effects may be linked to untracked chemicals.
Consider, for example trimethylamine N-oxide (TMAO). Recent studies have found that patients with stable
coronary heart disease had a four-fold greater risk of dying from any cause over the subsequent five years
if they had high blood levels of TMAO.

While TMAO and its precursor trimethylamine (TMA) naturally occur in fish and milk, important sources of TMAO
in the Western diet are *L*-carnitine and choline— all found in red meat.
These molecules are metabolized by gut bacteria into trimethylamine (TMA), which is then converted in
the liver to TMAO (Fig. 1). The Mediterranean diet, which regularly pairs red meat with fresh garlic,
derives some of its known health benefits from allicin, which blocks TMA production by gut bacteria,
ultimately lowering the TMAO concentration in plasma. Taken together, there are at least six distinct
biochemicals in our diet involved in TMAO pathway: *L*-carnitine, choline, trimethylamine (TMA), TMAO,
allicin, and 3,3-dimethylbutan-1- ol (DMB). Yet, only one of them, choline, is tracked and quantified in
nutritional databases.
The remaining four, despite the key roles they play in health, are effectively nutritional dark matter (Fig. 1).

Overall, 37 nutritional components of garlic can be linked to diseases according to the
Comparative Toxicogenomics Database (CTD). Indeed, garlic carries vitamins B1, B6, and C, and
the minerals manganese, copper, selenium, and calcium - nutrients whose deficiency or excess have been
linked to disease phenotypes like T2DM, Parkinson's disease and cardiomyopathies.
These links confirm the important role the currently tracked nutrients play in health (see :ref:`Supplementary Discussion 4 <SD4>`).
At the same time, the CTD reveals that 485 of the currently unquantified chemicals in garlic can also be
linked to multiple therapeutic effects, like the protective action of allicin in cardiovascular diseases discussed above.

There is a remarkable parallel between pre-genome biology and our current understanding of the
health implications of diet. Indeed, in the 1980s, detractors of the Human Genome Project insisted
that only the coding regions, representing 1.4% of all base pairs in our DNA, are worth the
cost of decoding, labelling the remaining 98.6% base pairs 'junk DNA'.
Yet, today it is estimated that 66% of disease-carrying variants are, in fact, in these non-coding regions.
Similarly, today the 150 nutrients tracked by national health agencies represent about 0.5% of
the 26,625 chemical compounds documented in food. The health implications of the nutritional components
are well documented. Yet, more than 99% of the biochemicals, many of which play a well-documented role in
health and disease, remain untracked by national databases, with the health implications of this largely
unexplored nutritional dark matter remaining largely unknown. The absence of information on these untracked
biochemicals could be responsible for inconsistencies in and the irreproducibility of published results,
as well as for missing health effects, and can also create spurious associations that are not replicable by meta-analysis.

.. figure:: /_static/media/img/2.png
   :figclass: align-center
   :class: no-scaled-link

   **Fig. 2 | Linking the diet to the genome and disease**. Our daily eating patterns define a unique biochemical barcode, representing a high-resolution
   description of each person’s individual biochemical exposure through his or her diet, or individual foodome. To assess the individual foodome in a reliable
   fashion, we can take advantage of the smartphone revolution and collect daily food diaries via image capture. Combined with genomics and disease
   histories, access to this full biochemical palette could help us expand the widely used genome-wide-association-study-based tools to account for the
   biochemical composition of our eating patterns, and systematically unveil the linkages between specific food biochemicals, genome variations and health

Advances in network medicine — a post-genome discipline that emphasizes the role of comprehensive
molecular interactions (comprising a molecular interaction network, or interactome) in the prevention and
treatment of disease — could help us to unveil systematically the mechanistic role of the wide array of
molecules found in our diet. Consider, for example, the polyphenol (-)-epigallocatechin 3-o-gallate (EGCG),
an abundant biochemical compound in green tea, with potential therapeutic effects on T2DM.
Network-based metrics reveal a proximity between 52 human proteins targets of EGCG and 83 proteins
associated with T2DM, offering multiple mechanistic pathways by which to account for the relationship
between green tea consumption and its many positive effects on health, such as the reduced disease
risk, and its glucose-lowering effects observed in *in vitro* and *in vivo* models.
Taken together, unveiling the nutritional dark matter could open up new strategies for discovering
the wide array of molecular mechanisms through which food affects health, helping us understand how
to use food as therapy, and aid the identification of food biochemicals with direct therapeutic impact.

Food affects our health through multiple molecular mechanisms: some chemicals serve as a direct source of
intermediates for human metabolism, while others, such as polyphenols, play a regulatory role.
Yet many food molecules also feed the microbiome in our gut, which metabolizes these compounds into other
species that can be further transformed by mammalian metabolism (e.g., TMA, TMAO).
Tracking the full chemical composition of the specific ingredients is also unavoidable if we wish to gain
a better understanding of the many ways by which the microbiome responds to the vast diversity of our diet,
and how best to alter the microbiome for therapeutic purposes.

Mapping out the Foodome
=======================

The current incomplete chemical profiling of food poses a number of fundamental scientific and
methodological challenges, limiting our ability to explore systematically the health implications of our
diet. Yet, the multiple 'known unknowns' of nutrition offer a potential roadmap by which to address them.
Indeed, a systematic mapping of the complete chemical composition of the food we consume, although costly,
is feasible, and could be greatly accelerated by recent advances in the use of big data and artificial
intelligence.

For example, the remarkable governmental and community efforts behind the databases like the USDA,
FooDB, Frida, PhenolExplorer, and eBasis have already resulted in a wealth of information on food
composition. Rapid advances in metabolic reconstructions and biochemical modeling enable us to infer
specific pathways from the genome, and through machine learning we can combine metabolic pathway information
with the existing food composition databases in a systematic fashion, potentially elucidating the missing chemicals.
Indeed, the closer two ingredients are on the phylogenetic tree, the more similar is their expected
metabolic pathway structure and biochemical composition. Machine learning is ideally suited to combine
the known chemical composition of chosen food ingredients over different taxonomical branches with the
list of orthologous enzymes in sequenced organisms; the missing chemical information can then be elucidated
by learning the appropriate distance metric between organisms and clustering correlated groups of pathways
and biochemicals. Such efforts, taking full advantage of existing knowledge, could offer experimentally
verifiable predictions about the missing chemicals and their concentration.

Yet, part of the challenge is experimental: the time-consuming, low-throughput, structural chemical tools
(spectroscopic methods, nuclear magnetic resonance, mass spectrometry, and so on) may need to be
fundamentally reengineered into high-throughput methods that can scan food with sufficient chemical
resolution and sensitivity, helping to catalogue the presence and the concentration of the vast array of
currently unquantified chemical compounds in the food supply. Such efforts are complemented by 'Foodomics',
a movement aiming to bring omics-technology to the systematic exploration of food.

Cooking and food processing alter the chemical composition of food, adding chemicals that are absent in
raw ingredients and transforming others, from emulsifiers to new lipids. Some of these changes have well
documented health implications, like the presence of acrylamide, a carcinogenic compound, in fried and
baked goods and in coffee. While the impact of food processing on basic nutritional components is well
studied, little is known about the impact of processing on the thousands of chemicals found in the
nutritional dark matter. Equally important, we must account for the numerous toxins added to food during
cooking, preservation, packaging, or accumulated in food according to the environmental production
conditions, and their effect on health, such as the well documented toxicity of the highly reactive
aldehydes or of persistent organic pollutants.

For nutrition to compete with genetics in accuracy, reach and impact, we must organize the information on
eating patterns to fit the big-data platform that fuels advances in this digital age of biomedicine.
Indeed, our eating patterns are digital — each of us consumes a weighted subset of chemicals found in
the food supply. The precise subset of chemicals to which each individual is exposed defines that person's
individual nutritional-chemical 'barcode', or his or her 'foodome' (Fig. 2).
The determinants of this personal foodome are complex, from the food supply to personal choices,
modulated by geography, culture, and socio-economic status. Efforts to ensure the traceability of food,
allowing us to track the source and the production of the raw material introduced into the food chain,
together with the environmental and processing conditions modulating the individual foodome,
will also greatly enhance future research in this arena. Our ability to track the nutritional-chemical
barcode of each individual, and correlate it with individual genetic variations and health history,
could help merge nutrition with a precise digital and statistical platform similar to that which fueled
the spectacular advances in genomics. Such a platform could help us scan systematically for novel causal
mutation-chemical- health associations that are largely invisible to current hypothesis-driven research in nutrition.

To appreciate the transformative potential of a deeper quantitative understanding of the nutritional dark
matter, we must realize that our genetic predispositions to specific phenotypes and pathophenotypes can
conceivably be modified by these food-based molecules. Indeed, while currently we cannot change the genetic
basis for disease, we regularly modulate the activity of our subcellular networks through the food we eat,
diminishing the impact of some mutations and enhancing the role of others. This differential modulation of
subcellular networks explains why individuals with strong genetic predispositions to heart disease can
lower the chance of developing the disease by up to 70% with proper lifestyle choices,
within which dietary changes play a dominant role. This finding implies that an accurate mapping of our
full chemical exposure through our diet could lead to actionable information to improve health.
Recent trends in nutrition research, aiming to explore the synergies, competitions, and interactions
among the entire matrix of what constitutes a food product, increasingly acknowledge the complexity of
the problem, and the need for new tools to address it. We must embrace this irreducible complexity to be
able to integrate changes in the food supply, the role of microbiome, and personalized dietary patterns so
that we can eventually offer individually tailored food-based therapies and appropriate lifestyle choices
for disease prevention and lifespan optimization.

.. _chap2:

**********************
Supplementary Material
**********************

This brief SM clarifies the coverage of the various databases discussed in the Perspective.

.. _SD1:

Supplementary 1: USDA Nutritional Panel
=======================================

The USDA nutritional panel of 150 entries includes several families of chemical compounds like sugars,
fats and amino acids, quantified as cumulative class ("Sugars, total") or specific chemical
compound ("Fructose"), together with the caloric assessment of food, measured in kcal and kJ.
Since 2003 USDA has released additional databases focused on the flavonoids' content of selected foods,
extending the main panel to 188 nutritional components.
| Nutrients are sometimes reported in multiple units of measurement, as in the case of Vitamin A content,
calculated both in 𝜇g and international units IU, commonly used to quantify and compare vitamins,
hormones and blood metabolites according to their biological activity.
Here, all the statistics comparing chemical compounds across different databases were calculated
considering only nutrients whose concentration was expressed in g, mg, 𝜇g, true for 184 nutrients in
the USDA panel.

Only 142 of the 184 nutritional components can be associated with an inChI key, a textual identifier for
distinct chemical substances, providing a standard way to encode molecular information.
The remaining entries correspond to measurements for broad families of chemical compounds
(e.g. "Total lipid", "Fatty acids, total saturated").

.. _SD2:

Supplementary 2: FooDB Chemical Library
=======================================

FooDB represents the most comprehensive resource on food constituents, chemistry and biology.
As of 08/01/2019, its online chemical library includes 26,625 chemical compounds, many of which need
to be directly linked to specific food ingredients. We expect this number to increase in the future,
with more focus on the chemical composition of food. By using the downloadable version of the database
(sql data dump dated 06/29/2017) and selecting only compounds reliable enough to be exported in
the online library, we found 15,941compounds with at least one food association.
Overall, 85% of these chemicals remain unquantified, meaning that their concentration in specific
food ingredients remains unknown. The chemicals in the database are mainly lipids (fatty acids, 32%),
phenylpropanoids and polyketides (flavonoids, 11%), organooxygen compounds (carbohydrates and conjugates, 7%)
and organic acids and derivatives (amino acids and peptides, 5%).

.. _SD3:

Supplementary 3: Garlic composition in USDA, FooDB and FoodMine
===============================================================

*Raw garlic in USDA:* In the USDA database the nutrient assessment of raw garlic is reported under the entry "Garlic,
Raw" (id=11215). While the full report consists of 105 nutritional components, only 67 have values different from zero
(64 if we remove energy measurements and vitamins expressed in international units).

*Comparison between USDA, FooDB and FoodMine:* To unveil the chemical composition of garlic we used multiple related
food categories for each source: we considered "Garlic, raw" and "Spices, garlic powder" for USDA, and "Garlic"
and "Soft-necked Garlic" for FooDB.

To compare the different chemical descriptions, we needed to disambiguate the chemical nomenclature, leveraging the
PubChem database to address the naming differences, an extensive database of chemical compounds from NCBI that contains
information on compound synonyms. For this purpose, we queried all compound strings for FoodMine, FooDB, and USDA to
retrieve associated inChI key. By selecting the first 14 characters of the inChI key, we determined the code for the
structure of each chemical. Chemicals with identical structural code were considered identical and removed, thereby
filtering to unique chemical structures and omitting information regarding stereochemistry and ionization.
By restricting the assessment to the physical structure, the varying methodologies between the databases with respect
to stereochemistry and ionization were removed, allowing for objective comparisons between databases.
If no inChI key was found, we proceeded by string matching.

The results of the analysis are reported in Table 1, where we compare FoodMine to the union of FooDB and USDA, and
in which the chemical compounds are stratified by types of measurement: 'quantified', 'unquantified', and 'zero'
(the compound is reported as absent in the selected food).

The raw data and codes for the complete analysis are available on github, at https://github.com/fhooton/FoodMine.

.. _ST1:

.. table:: *Table 1: Comparison of FoodMine with USDA and FooDB*
   :align: center
   :width: 100%
   :widths: auto
   :class: align-center

   +------------------------------+-------------------------+--------------------------+--------------------+-----------------+
   |                              | quantified in FoodMine  | unquantified in FoodMine | zeros in FoodMine  | not in FoodMine |
   +==============================+=========================+==========================+====================+=================+
   | quantified in (USDA FooDB)   | 68                      | 4                        | 0                  | 105             |
   +------------------------------+-------------------------+--------------------------+--------------------+-----------------+
   | unquantified in (USDA FooDB) | 35                      | 6                        | 0                  | 1767            |
   +------------------------------+-------------------------+--------------------------+--------------------+-----------------+
   | zeros in (USDA FooDB)        | 2                       | 1                        | 0                  | 48              |
   +------------------------------+-------------------------+--------------------------+--------------------+-----------------+
   | not in (USDA FooDB)          | 96                      | 74                       | 3                  |                 |
   +------------------------------+-------------------------+--------------------------+--------------------+-----------------+

.. _SD4:

Supplementary 4: Health effects
===============================

We used the number of manually curated health associations from CTD (download date 3/25/2019) to compare health
relevance across FoodMine, FooDB, and USDA. For this analysis, we counted the number of chemical compounds
with "markers/mechanisms" or "therapeutic" annotations. Similarly to the disambiguation step necessary to
compare FoodMine, FooDB, and USDA, we queried all the compounds in CTD to retrieve their inChI key.
We improved our search by directly querying PubChem for MeSH ids, provided by CTD.
We were then able to calculate the number of chemical compounds in garlic with disease relevance according to the
three databases, stratifying by types of measurement. The number of chemical compounds with health associations covered
by USDA is 37, while for the 2,306 chemical compounds tracked by FooDB we find 89 quantified compounds and 485
unquantified compounds with annotations in CTD.



.. toctree::
   :maxdepth: 1
