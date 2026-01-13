import importlib.util
import sys
import types


def ensure_distutils() -> None:
    """Ensure distutils.version.LooseVersion is available for legacy dependencies."""

    if importlib.util.find_spec("distutils") is not None:
        return

    try:
        setuptools_spec = importlib.util.find_spec("setuptools")
    except ModuleNotFoundError:
        setuptools_spec = None

    if setuptools_spec and importlib.util.find_spec("setuptools._distutils") is not None:
        import setuptools._distutils as distutils

        sys.modules.setdefault("distutils", distutils)
        sys.modules.setdefault("distutils.version", distutils.version)
        return

    if importlib.util.find_spec("packaging.version") is not None:
        from packaging.version import Version

        distutils = types.ModuleType("distutils")
        version_module = types.ModuleType("distutils.version")

        class LooseVersion:
            def __init__(self, vstring: str = "") -> None:
                self.vstring = vstring
                self._parsed = Version(vstring) if vstring else Version("0")

            def __repr__(self) -> str:
                return f"LooseVersion ('{self.vstring}')"

            def __str__(self) -> str:
                return self.vstring

            def _cmp(self, other) -> int:
                other_version = (
                    other._parsed
                    if isinstance(other, LooseVersion)
                    else Version(str(other))
                )
                if self._parsed < other_version:
                    return -1
                if self._parsed > other_version:
                    return 1
                return 0

            def __lt__(self, other) -> bool:
                return self._cmp(other) < 0

            def __le__(self, other) -> bool:
                return self._cmp(other) <= 0

            def __eq__(self, other) -> bool:
                return self._cmp(other) == 0

            def __ge__(self, other) -> bool:
                return self._cmp(other) >= 0

            def __gt__(self, other) -> bool:
                return self._cmp(other) > 0

        version_module.LooseVersion = LooseVersion
        distutils.version = version_module
        sys.modules.setdefault("distutils", distutils)
        sys.modules.setdefault("distutils.version", version_module)
        return

    distutils = types.ModuleType("distutils")
    version_module = types.ModuleType("distutils.version")

    class LooseVersion:
        def __init__(self, vstring: str = "") -> None:
            self.vstring = vstring
            self._parts = self._parse(vstring)

        def _parse(self, vstring: str) -> list[object]:
            parts: list[object] = []
            for part in vstring.replace("-", ".").split("."):
                parts.append(int(part) if part.isdigit() else part)
            return parts

        def __repr__(self) -> str:
            return f"LooseVersion ('{self.vstring}')"

        def __str__(self) -> str:
            return self.vstring

        def _cmp(self, other) -> int:
            other_parts = (
                other._parts
                if isinstance(other, LooseVersion)
                else LooseVersion(str(other))._parts
            )
            if self._parts < other_parts:
                return -1
            if self._parts > other_parts:
                return 1
            return 0

        def __lt__(self, other) -> bool:
            return self._cmp(other) < 0

        def __le__(self, other) -> bool:
            return self._cmp(other) <= 0

        def __eq__(self, other) -> bool:
            return self._cmp(other) == 0

        def __ge__(self, other) -> bool:
            return self._cmp(other) >= 0

        def __gt__(self, other) -> bool:
            return self._cmp(other) > 0

    version_module.LooseVersion = LooseVersion
    distutils.version = version_module
    sys.modules.setdefault("distutils", distutils)
    sys.modules.setdefault("distutils.version", version_module)
