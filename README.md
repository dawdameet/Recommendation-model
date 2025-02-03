### **Mathematical Formulation**

#### **1. Feature Space**
Each item $ F(i) $ is represented as a 3-dimensional vector:
$$
F(i) = [p, c, b]
$$
Where:
- $ p $: Discretized price (e.g., $1$ for low-priced, $2$ for high-priced).
- $ c $: Category (e.g., $1$ for shoes, $2$ for clothes, $3$ for accessories).
- $ b $: Brand (e.g., $1$ for Nike, $2$ for Adidas, $3$ for Puma).

---

#### **2. Liked and Disliked Items**
- Liked items: $ L = \{i_1, i_2, \dots, i_n\} $
- Disliked items: $ D = \{j_1, j_2, \dots, j_m\} $

---

#### **3. User Profile Calculation**
The user profile $ U $ is calculated as:
$$
U = w_L \cdot \frac{\sum_{i \in L} F(i)}{|L|} - w_D \cdot \frac{\sum_{j \in D} F(j)}{|D|}
$$
Where:
- $ w_L + w_D = 1 $ (weights for liked and disliked items).
- $ |L| $: Number of liked items.
- $ |D| $: Number of disliked items.

Breaking it down:
1. **Average of liked items:**
   $$
   \text{Liked Average} = \frac{\sum_{i \in L} F(i)}{|L|}
   $$

2. **Average of disliked items:**
   $$
   \text{Disliked Average} = \frac{\sum_{j \in D} F(j)}{|D|}
   $$

3. **Final user profile:**
   $$
   U = w_L \cdot \text{Liked Average} - w_D \cdot \text{Disliked Average}
   $$

---

#### **4. Cosine Similarity**
For an item $ F(k) $, the cosine similarity with the user profile $ U $ is:
$$
\text{Cosine Similarity} = \frac{U \cdot F(k)}{\|U\| \cdot \|F(k)\|}
$$
Where:
- Dot product:
  $$
  U \cdot F(k) = \sum_{i=1}^3 U_i \cdot F(k)_i
  $$
- Magnitude of $ U $:
  $$
  \|U\| = \sqrt{\sum_{i=1}^3 U_i^2}
  $$
- Magnitude of $ F(k) $:
  $$
  \|F(k)\| = \sqrt{\sum_{i=1}^3 F(k)_i^2}
  $$

---

#### **5. Decision Rule**
Based on the cosine similarity $ \text{sim} $:
- If $ \text{sim} < 0 $: User might not like the product.
- If $ 0 \leq \text{sim} < 0.5 $: User might like the product (low chances).
- If $ \text{sim} \geq 0.5 $: User will like the product (high chances).
