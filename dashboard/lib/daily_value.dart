class DailyValue {
  final DateTime date;
  final int value;
  DailyValue(String dateStr, this.value) : date = DateTime.parse(dateStr) {
    if (value < 0) throw ArgumentError.value("");
  }
}
