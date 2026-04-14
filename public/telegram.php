<?php
/**
 * Telegram Form Handler
 * Captures form POST data and sends it to a specified Telegram Group/User
 */

header('Content-Type: application/json');
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST");

// ==========================================
// 1. УКАЖИТЕ ВАШИ ДАННЫЕ TELEGRAM НИЖЕ
// ==========================================
$TELEGRAM_TOKEN = "ВАШ_ТОКЕН_БОТА";
$CHAT_ID = "ВАШ_CHAT_ID";
// ==========================================

// If the user hasn't set the token yet, return an error safely
if ($TELEGRAM_TOKEN === "ВАШ_ТОКЕН_БОТА" || empty($TELEGRAM_TOKEN)) {
    echo json_encode(["status" => "error", "message" => "Telegram Bot Token is not configured."]);
    exit;
}

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    echo json_encode(["status" => "error", "message" => "Invalid request method"]);
    exit;
}

// 2. Сбор данных из POST запроса
$name    = isset($_POST['name']) ? trim($_POST['name']) : '';
$phone   = isset($_POST['phone']) ? trim($_POST['phone']) : '';
$service = isset($_POST['service']) ? trim($_POST['service']) : 'Общая консультация';
$comment = isset($_POST['comment']) ? trim($_POST['comment']) : '';

// Проверка обязательных полей
if (empty($phone)) {
    echo json_encode(["status" => "error", "message" => "Телефон обязателен для заполнения."]);
    exit;
}

// Формируем красивое сообщение для Telegram
$messageText = "🚨 <b>Новая заявка с сайта EuroStatus!</b>\n\n";

if (!empty($name)) {
    $messageText .= "👤 <b>Имя:</b> " . htmlspecialchars($name) . "\n";
}

$messageText .= "📞 <b>Телефон:</b> " . htmlspecialchars($phone) . "\n";
$messageText .= "💼 <b>Услуга:</b> " . htmlspecialchars($service) . "\n";

if (!empty($comment)) {
    $messageText .= "💬 <b>Комментарий:</b> " . htmlspecialchars($comment) . "\n";
}

$messageText .= "\n⏱ <i>Время: " . date("Y-m-d H:i:s") . "</i>";

// 3. Отправка в Telegram API
$telegramApiUrl = "https://api.telegram.org/bot{$TELEGRAM_TOKEN}/sendMessage";

$data = [
    'chat_id' => $CHAT_ID,
    'text' => $messageText,
    'parse_mode' => 'HTML',
    'disable_web_page_preview' => true
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $telegramApiUrl);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
// Внимание: Отключение проверки SSL может понадобиться на старых хостингах, но лучше оставить как есть
// curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false); 

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($httpcode == 200) {
    echo json_encode(["status" => "success", "message" => "Заявка успешно отправлена!"]);
} else {
    echo json_encode(["status" => "error", "message" => "Ошибка при отправке в Telegram.", "tg_response" => $response]);
}
?>
