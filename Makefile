.DEFAULT_GOAL := figures

PYTHON ?= python3

.PHONY: figures clean previews

# Generate fresh inflation figures (SVG) into ./output
figures:
	$(PYTHON) main.py

# Copy generated figures into docs/previews for README rendering
previews: figures
	mkdir -p docs/previews
	@for f in inflation_comparison ecb_interest_rates inflation_difference statistics_comparison historical_comparison eu_inflation_heatmap; do \
		if [ -f output/$$f.svg ]; then \
			cp output/$$f.svg docs/previews/$$f.svg; \
			echo "Updated docs/previews/$$f.svg"; \
		else \
			echo "Missing output/$$f.svg; run 'make figures' to generate"; \
		fi; \
	done

# Remove generated artifacts
clean:
	rm -rf output
