"""
Factory Method is a creational design pattern that provides an interface for
creating objects in a superclass, but allows subclasses to alter the type of
objects that will be created.

This pattern focus on separete the object creation from use.
"""

from abc import ABC, abstractmethod


class ImageDataExporter(ABC):
    """
    << Interface A >>
    Representation of an image exporter.
    """

    @abstractmethod
    def pre_process_data(self, image):
        """First, pre-process image data before export it."""

    @abstractmethod
    def export_data(self, folder):
        """Export the pre-processed data to a folder."""


class GrayScaleImageDataExporter(ImageDataExporter):
    """
    << Concrete Product AA >>
    Gray scale pre-process image data exporter.
    """

    def pre_process_data(self, image):
        print("Pre-process image for gray scale.")

    def export_data(self, folder):
        print(f"Export image data in gray scale to {folder}")


class NoiseReductionImageDataExporter(ImageDataExporter):
    """
    << Concrete Product AB >>
    Noise reduction pre-process image data exporter.
    """

    def pre_process_data(self, image):
        print("Pre-process image for noise reduction.")

    def export_data(self, folder):
        print(f"Export image data with less noise to {folder}")


class AudioDataExporter(ABC):
    """
    << Interface B >>
    Representation of an audio exporter.
    """

    @abstractmethod
    def pre_process_data(self, audio):
        """First pre-process audio data before export it."""

    @abstractmethod
    def export_data(self, folder):
        """Export the pre-processed data to a folder."""


class ResamplingAudioDataExporter(AudioDataExporter):
    """
    << Concrete Product BA >>
    Resampling pre-process audio data exporter.
    """

    def pre_process_data(self, audio):
        print("Pre-process audio for resampling.")

    def export_data(self, folder):
        print(f"Export audio data with resampling to {folder}")


class FilterAudioDataExporter(AudioDataExporter):
    """
    << Concrete Product BB >>
    Filter pre-process audio data exporter.
    """

    def pre_process_data(self, audio):
        print("Pre-process audio for filtering.")

    def export_data(self, folder):
        print(f"Export filtered audio data to {folder}")


class ExporterFactory(ABC):
    """
    << Creator >>
    This factory class represents a combination of different types of image
    and audio exporters. The goal is to create the instances we need.

    In this example, the factory produces two different products: image data
    exporters and audio data exporters.
    """

    def get_image_data_exporter(self) -> ImageDataExporter:
        """Returns a new image data exporter."""

    def get_audio_data_exporter(self) -> AudioDataExporter:
        """Returns a new audio data exporter."""


class OptionAExporterFactory(ExporterFactory):
    """
    << Concrete Creator Type A >>
    Factory to provide type A exports configuration.
    """

    def get_image_data_exporter(self) -> ImageDataExporter:
        return GrayScaleImageDataExporter()

    def get_audio_data_exporter(self) -> AudioDataExporter:
        return ResamplingAudioDataExporter()


class OptionBExporterFactory(ExporterFactory):
    """
    << Concrete Creator Type B >>
    Factory to provide type B exports configuration.
    """

    def get_image_data_exporter(self) -> ImageDataExporter:
        return NoiseReductionImageDataExporter()

    def get_audio_data_exporter(self) -> AudioDataExporter:
        return FilterAudioDataExporter()


def choose_exporter_type() -> ExporterFactory:
    """Constructs an exporter factory based on the user input preferences."""
    factories = {
        "A": OptionAExporterFactory(),
        "B": OptionBExporterFactory(),
    }
    while True:
        t = input("Choose the exporter type: (A) or (B)\n")
        if t in factories.keys():
            return factories[t]
        print("Please, enter a valid option. (A) or (B).")


def main() -> None:
    factory = choose_exporter_type()

    image_exporter = factory.get_image_data_exporter()
    audio_exporter = factory.get_audio_data_exporter()

    image_exporter.pre_process_data(image=".jpeg")
    audio_exporter.pre_process_data(audio=".mp3")

    image_exporter.export_data(folder="Downloads/")
    audio_exporter.export_data(folder="Downloads/")


if __name__ == "__main__":
    main()
