
from django.http import HttpResponse

def get_name(request):
    html="""
       <!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <title>Ismni Chiqarish</title>
</head>
<body>
    <!-- Foydalanuvchi ism kiritishi uchun input maydoni -->
    <input type="text" id="nameInput" placeholder="Enter your name" required>

    <!-- Tugma, bosilganda ismni chiqarish -->
    <button onclick="showName()">Ko'rsat</button>

    <!-- Ma'lumotni chiqarish uchun bo'sh div -->
    <div id="output"></div>

    <!-- JavaScript funksiyasi -->
    <script>
        function showName() {
            // Input maydonidan qiymatni olish
            var name = document.getElementById('nameInput').value;

            // Agar qiymat bo'sh bo'lsa, xabar chiqarish
            if (name.trim() === '') {
                document.getElementById('output').innerText = 'Iltimos, ismingizni kiriting.';
            } else {
                // Qiymatni div ichiga chiqarish
                document.getElementById('output').innerText = 'Kiritilgan ism: ' + name;
            }
        }
    </script>
</body>
</html>

    
    """
    return HttpResponse(html)
def get_age(request):
    html="""
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <title>Tug'ilgan Yilni Chiqarish</title>
</head>
<body>
    <!-- Tug'ilgan yilni kiritish uchun input maydoni -->
    <label for="birthYear">Tug'ilgan yil:</label>
    <input type="number" id="birthYear" placeholder="YYYY" min="1900" max="2023" required>

    <!-- Tugma, bosilganda tug'ilgan yilni chiqarish -->
    <button onclick="showBirthYear()">Ko'rsat</button>

    <!-- Ma'lumotni chiqarish uchun bo'sh div -->
    <div id="output"></div>

    <!-- JavaScript funksiyasi -->
    <script>
        function showBirthYear() {
            // Input maydonidan tug'ilgan yil qiymatini olish
            var birthYear = document.getElementById('birthYear').value;

            // Agar qiymat bo'sh bo'lsa yoki noto'g'ri bo'lsa, xabar chiqarish
            if (birthYear.trim() === '') {
                document.getElementById('output').innerText = 'Iltimos, tug\'ilgan yilingizni kiriting.';
            } else {
                // Tug'ilgan yilni ekranga chiqarish
                document.getElementById('output').innerText = 'Tug\'ilgan yilingiz: ' + birthYear;
            }
        }
    </script>
</body>
</html>

    """
    return HttpResponse(html)