

def auto_delete_file_img_on_delete(sender, instance, **kwargs):
    """Удаляет файл из файловой системы при удалении объекта."""
    if instance.image:
        instance.image.delete(False)


def auto_delete_file_img_on_change(sender, instance, **kwargs):
    """Удаляет старый файл из файловой системы при обновлении записи с новым файлом."""
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        old_file.delete(False)